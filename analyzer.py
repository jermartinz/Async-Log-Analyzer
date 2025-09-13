import asyncio
import aiofiles



async def file_analysis(log_files):
    count_event = {"INFO": 0, "WARN": 0, "ERROR": 0, "DEBUG": 0}
    first_error = None
    last_error = None
    max_warn_consecutives = 0
    current_warn = 0
    
    async with aiofiles.open(log_files, 'r', encoding='utf-8') as file:
        async for line in file:
            sections = line.strip().split(' ', 3)
            if len(sections) >= 4:
                _, _, level, _ = sections
                
                if level in count_event:
                    count_event[level] += 1
                
                # Lógica de errores
                if level == "ERROR":
                    complete_line = line.strip()
                    if first_error is None:
                        first_error = complete_line
                    last_error = complete_line
                    current_warn = 0
                
                
                elif level == "WARN":
                    current_warn += 1
                    if current_warn > max_warn_consecutives:
                        max_warn_consecutives = current_warn
                else:
                    current_warn = 0
                
                if count_event["INFO"] % 100 == 0:
                    await asyncio.sleep(0)
    
    return {
        'file': log_files,
        'counts': count_event,
        'firs_error': first_error,
        'last_error': last_error,
        'max_warn_consecutives': max_warn_consecutives
    }

async def multi_file_analysis(log_files):
    tasks = [file_analysis(log_file) for log_file in log_files]
    results = await asyncio.gather(*tasks)
    return results

import sys
import asyncio

# Import the analyzer module safely
try:
    import analyzer as an
except ImportError as e:
    print(f"Error importing module: {e}")
    sys.exit(1)

async def main():
    """Main function to run the log analysis."""

    # Analyze a single file
    result = await an.file_analysis('sample.log')
    print(f"File: {result['file']}")
    print(f"Counts: {result['counts']}")
    print(f"First Error: {result['firs_error']}")
    print(f"Last Error: {result['last_error']}")
    print(f"Max Consecutive WARN: {result['max_warn_consecutives']}")
    print("-----")

    # Analyze multiple files
    files = ['sample.log', 
            'sample_1.log', 'sample_2.log', 
            'sample_3.log']
    multi_results = await an.multi_file_analysis(files)
    for res in multi_results: 
        print(f"File: {res['file']}")
        print(f"Counts: {res['counts']}")
        print(f"First Error: {res['firs_error']}")
        print(f"Last Error: {res['last_error']}")
        print(f"Max Consecutive WARN: {res['max_warn_consecutives']}")
        print("-----")


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())

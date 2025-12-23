import argparse

def calculate_bandwidth_gbps(hard_drives: int, data_size_tb: float, days: float) -> float:
    # ==============================================================================
    # STEP 1: CALCULATE TOTAL DATA SIZE
    # ==============================================================================
    # Simple math: Number of drives multiplied by size of each drive
    total_tb = hard_drives * data_size_tb
    
    # ==============================================================================
    # STEP 2: CONVERT EVERYTHING TO BYTES (THE RAW NUMBER)
    # ==============================================================================
    # NOTE: The exam template says "1 TB = 1000^4 bytes". This is DECIMAL standard.
    #
    # SCENARIO A: If he says "Use Binary / IEC units (1 TB = 1024^4)"
    # -> Change the '1000' below to '1024'.
    #
    # SCENARIO B: If the drives are in GB, not TB
    # -> Change '1000**4' to '1000**3'.
    # ------------------------------------------------------------------------------
    total_bytes = total_tb * (1000**4)


    # ==============================================================================
    # STEP 3: CALCULATE TOTAL TIME IN SECONDS
    # ==============================================================================
    # We need to convert the input time into Seconds.
    # Current formula: Days * 24 (Hours) * 60 (Minutes) * 60 (Seconds)
    #
    # SCENARIO C: If input is in HOURS (not Days)
    # -> DELETE the '* 24'. Make it: days * 60 * 60
    #
    # SCENARIO D: If input is in MINUTES
    # -> DELETE the '* 24 * 60'. Make it: days * 60
    # ------------------------------------------------------------------------------
    seconds = days * 24 * 60 * 60


    # ==============================================================================
    # STEP 4: DO THE DIVISION (BYTES PER SECOND)
    # ==============================================================================
    # This gives us the raw speed in Bytes/sec. Do not touch this line.
    bytes_per_second = total_bytes / seconds
    
    
    # ==============================================================================
    # STEP 5: CONVERT TO THE FINAL UNIT (GB/s, MB/s, etc)
    # ==============================================================================
    # We need to divide the big number to make it readable.
    #
    # SCENARIO E: He asks for MB/s (Megabytes)
    # -> Change '1000**3' to '1000**2'
    #
    # SCENARIO F: He asks for Mbps (Megabits - notice the small 'b')
    # -> Multiply 'bytes_per_second' by 8 first!
    # ------------------------------------------------------------------------------
    # Current setting: GB/s (1000 power of 3)
    final_speed = bytes_per_second / (1000**3)

    return final_speed

def main():
    # This section handles the command line inputs (e.g., --days 3)
    # You usually don't need to touch this unless he asks for a FILE input.
    parser = argparse.ArgumentParser(
        description="Calculate the bandwidth of Alice's car (data transfer rate in GB/s)."
    )
    parser.add_argument(
        "--hard-drives",
        type=int,
        required=True,
        help="Number of hard drives Alice is carrying.",
    )
    parser.add_argument(
        "--data-size",
        type=float,
        required=True,
        help="Size of each hard drive in TB (terabytes).",
    )
    parser.add_argument(
        "--days",
        type=float,
        required=True,
        help="Number of days Alice spends driving.",
    )

    args = parser.parse_args()

    # --- IF HE ASKS TO READ FROM A FILE INSTEAD OF COMMAND LINE ---
    # Comment out the 'args = ...' block above and uncomment this:
    #
    # with open("input.txt", "r") as f:
    #     content = f.read().split() 
    #     # Assuming file has: 100 16 3 (separated by space)
    #     val_drives = int(content[0])
    #     val_size = float(content[1])
    #     val_days = float(content[2])
    #     gbps = calculate_bandwidth_gbps(val_drives, val_size, val_days)
    # ---------------------------------------------------------------

    # Run the math function
    gbps = calculate_bandwidth_gbps(args.hard_drives, args.data_size, args.days)

    # Print results in the format expected by the exam template
    print("=== Alice's Car Bandwidth Calculation ===")
    print(f"Hard drives        : {args.hard_drives}")
    print(f"Data size per drive: {args.data_size} TB")
    print(f"Travel time        : {args.days} days")
    print()
    print(f"Bandwidth          : {gbps:.3f} GB/s")

if __name__ == "__main__":
    main()
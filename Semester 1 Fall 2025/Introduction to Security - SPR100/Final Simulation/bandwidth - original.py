import argparse


def calculate_bandwidth_gbps(hard_drives: int, data_size_tb: float, days: float) -> float:
    """
    Calculate bandwidth of Alice's car in GB/s only.

    - hard_drives: number of hard drives
    - data_size_tb: size of each drive in TB
    - days: travel time in days
    """
    # Use decimal units: 1 TB = 1000^4 bytes
    bytes_per_tb = 0

    total_bytes = 0

    # Time in seconds
    seconds = 1

    bytes_per_second = total_bytes / seconds
    gb_per_second = bytes_per_second / (1000**3)  # GB/s

    return gb_per_second


def main():
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

    gbps = calculate_bandwidth_gbps(args.hard_drives, args.data_size, args.days)

    print("=== Alice's Car Bandwidth Calculation ===")
    print(f"Hard drives        : {args.hard_drives}")
    print(f"Data size per drive: {args.data_size} TB")
    print(f"Travel time        : {args.days} days")
    print()
    print(f"Bandwidth          : {gbps:.3f} GB/s")


if __name__ == "__main__":
    main()

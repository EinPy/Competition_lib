import sys
input = sys.stdin.read
def main():
    data = input().strip().split()
    n = int(data[0])
    matrix = [list(map(int, list(data[i+1]))) for i in range(n)]
    
    # Compute prefix sums for quick area sum calculation
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
    for r in range(1, n+1):
        for c in range(1, n+1):
            prefix_sum[r][c] = matrix[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]
    
    def get_sum(r1, c1, r2, c2):
        return (prefix_sum[r2+1][c2+1] - prefix_sum[r1][c2+1] - prefix_sum[r2+1][c1] + prefix_sum[r1][c1])

    # Recursive function to compute the minimum difference
    def rec(r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            return 0 if matrix[r1][c1] == out[r1][c1] else 1
        
        midr = (r1 + r2) // 2
        midc = (c1 + c2) // 2
        best_diff = float('inf')
        
        # Try different configurations for the quadrants
        for white_index in range(4):
            local_diff = 0
            configs = [(r1, c1, midr, midc), (r1, midc+1, midr, c2), (midr+1, c1, r2, midc), (midr+1, midc+1, r2, c2)]
            counts = [get_sum(*configs[i]) for i in range(4)]
            areas = [(configs[i][2] - configs[i][0] + 1) * (configs[i][3] - configs[i][1] + 1) for i in range(4)]
            
            for i in range(4):
                if i == white_index:
                    local_diff += areas[i] - counts[i]  # cost to paint white
                else:
                    local_diff += counts[i]  # cost to paint black
            
            # Recurse on the two remaining quadrants that are not fully painted
            for i in range(4):
                if i != white_index:
                    local_diff += rec(*configs[i])
            
            best_diff = min(best_diff, local_diff)
        
        return best_diff

    # Output array and difference calculation
    out = [[0] * n for _ in range(n)]
    diff = rec(0, 0, n-1, n-1)
    
    # Print the result
    print(diff)
    for row in out:
        print("".join(map(str, row)))

if __name__ == "__main__":
    main()

import sys
import json

def main():
    # Usage: python generate_comment.py --thread_id [ID]
    thread_id = None
    if "--thread_id" in sys.argv:
        idx = sys.argv.index("--thread_id")
        if idx + 1 < len(sys.argv):
            thread_id = sys.argv[idx + 1]

    if not thread_id:
        print("Usage: python generate_comment.py --thread_id [ID]")
        sys.exit(1)

    print(f"[*] Generating comment for thread: {thread_id}")
    
    # Mock comment generation
    comment = "I've been using this for a while and it's honestly a game changer. Super easy to set up and the support is great. Definitely worth checking out!"
    
    print("\n--- Suggested Comment ---")
    print(comment)
    print("------------------------\n")

if __name__ == "__main__":
    main()

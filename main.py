import argparse

def main():
    parser = argparse.ArgumentParser(description='CLI for CITADEL')
    # Add your CLI arguments here
    parser.add_argument('--example', type=str, help='An example argument')
    args = parser.parse_args()
    
    # Implement your CLI functionality here
    print(f'Example argument value: {args.example}')

if __name__ == '__main__':
    main()
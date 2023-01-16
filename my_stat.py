import sys
import statistics

def stat(list, text):
    if len(list) > 0:
        print(f'{text}:')
        print(f'mean: {statistics.mean(list)}', end=' ')
        print(f'std: {statistics.stdev(list)}', end=' ')
        print(f'min: {min(list)}', end=' ')
        print(f'max: {max(list)}', end=' ')
        print(f'n: {len(list)}')

def main(filenames):
    combined = []
    for filename in filenames:
        with open(filename, 'r') as lines:
            individual = [int(line.replace('\n', '')) for line in lines]
        combined += individual
        stat(individual, filename)
    stat(combined, 'combined')

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except:
        print('Something went wrong!')

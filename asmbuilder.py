import sys
import subprocess


def run(file_name, file_out):
    try:
        # build the asm file
        # works on linux for now
        bin_file :str = input("Enter the name of the binary file you want after linking: ")
        subprocess.run(['as', '-o', file_out, file_name], stdout=subprocess.PIPE, text=True)
        print(f'have assembled the output{file_out}')
        # linker
        subprocess.run(['ld', '-o', bin_file, file_out], stdout=subprocess.PIPE, text=True)
        print(f'have linked the output to the binary {bin_file}')
    except (subprocess.SubprocessError, subprocess.CalledProcessError) as e:
        print(f'{e}\n')


def main():
    if len(sys.argv) < 3:
        print("enter the right amount of parameter ")
    else:
        file_out = sys.argv[1]
        file_name = sys.argv[2]
        run(file_name, file_out)


if __name__ == '__main__':
    main()


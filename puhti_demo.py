# Test what CPUs and GPUs you have booked for your batch job

import torch
import os

def check_my_gpu():
    """ Check if system has GPU available and print possible GPU details."""
    gpu_available = torch.cuda.is_available()
    if gpu_available:
        print("\nGPU found!")
        number_of_gpus = torch.cuda.device_count()
        print("Number of GPUs: {}".format(torch.cuda.device_count()))
        print("GPU types:")
        for i in range(number_of_gpus):
            print("GPU {} type: {}".format(i, torch.cuda.get_device_name(i)))
    else:
        print("No GPUs available!")

def check_my_cpu():
    """ Check number of CPUs in partition and how many you are booking."""
    print("\nTotal number of CPU cores in the system: {}".format(os.cpu_count()))
    print("You are booking {} CPU cores.".format(len(os.sched_getaffinity(0))))

def create_file():
    """ Save simple text file to remember.txt."""
    f = open("remember.txt", "w")
    f.write("Remember following:\n\n")
    f.write("Things you print will go to file defined in run_script\n")
    f.write("In this example prints are saved to output.txt\n\n")
    f.write("Saved results will be saved similarly as in normal computer\n")
    f.write("Like this file is saved in remember.txt")
    f.close()

def main():
    check_my_cpu()
    check_my_gpu()
    create_file()

if __name__ == "__main__":
    main()
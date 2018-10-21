def findBestFit(size1, size2, space):
    ''' figures out the largest combination of files that fits on a storage device.
      The function should return 3 if both files fit together, the file number (1 or 2)
      corresponding to the longest file that fits by itself (1 if the files are the same size),
      or 0 if neither file fits on the storage device.
      Your function must have only one return statement.
     '''
    # write you code here
    num = 0
    if size1 + size2 <= space:
        num = 3
    if size1 == size2:
        num = 1
    else:
        if size1 < space:
            num = 1
        if size2 < space and size2 > size1:
            num = 2
    return num


def main():
    # you can call the function to test it here
    print(findBestFit(50, 75, 100))


if __name__ == "__main__":
    main()

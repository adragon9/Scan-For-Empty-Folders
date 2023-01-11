import os
import datetime

if __name__ == "__main__":
    emptyFileCount = 0
    totalFileCount = 0
    drive = input("Enter drive letter: ")
    drive = str.upper(drive)

    ignore = ["{}:\\Users\\{}\\Desktop".format(drive, os.getlogin()),
              "{}:\\Users\\{}\\Documents".format(drive, os.getlogin()),
              "{}:\\Users\\{}\\Downloads".format(drive, os.getlogin()),
              "{}:\\Users\\{}\\Music".format(drive, os.getlogin()),
              "{}:\\Users\\{}\\Pictures".format(drive, os.getlogin()),
              "{}:\\Users\\{}\\Videos".format(drive, os.getlogin())]

    while len(drive) > 1:
        print("No, do it again.")
        drive = input("Enter drive letter: ")

    with open("{}_Drive_log-{}.txt".format(drive, datetime.datetime.timestamp(datetime.datetime.now())), 'w') as log:
        if os.path.exists("{}:\\Users".format(drive)):
            if os.path.exists("{}:\\Users\\{}\\Desktop".format(drive, os.getlogin())) is True:
                print("Desktop Found")
                for root, dirnames, files in os.walk("{}:\\Users\\{}\\Desktop".format(drive, os.getlogin())):
                    # print("PATH-->", root)
                    if not files and not dirnames:
                        print("EMPTY FILE-->", root)
                        log.write("{}\n".format(root.encode("utf-8")))
                        emptyFileCount = emptyFileCount + 1
                    totalFileCount = totalFileCount + 1
            else:
                print("Desktop Not Found")

            print("Files processed... {}".format(totalFileCount))

            if os.path.exists("{}:\\Users\\{}\\Documents".format(drive, os.getlogin())) is True:
                print("Documents Found")
                for root, dirnames, files in os.walk("{}:\\Users\\{}\\Documents".format(drive, os.getlogin())):
                    # print("PATH-->", root)
                    if not files and not dirnames:
                        print("EMPTY FILE-->", root)
                        log.write("{}\n".format(root.encode("utf-8")))
                        emptyFileCount = emptyFileCount + 1
                    totalFileCount = totalFileCount + 1
            else:
                print("Documents Not Found")

            print("Files processed... {}".format(totalFileCount))

            if os.path.exists("{}:\\Users\\{}\\Downloads".format(drive, os.getlogin())) is True:
                print("Downloads Found")
                for root, dirnames, files in os.walk("{}:\\Users\\{}\\Downloads".format(drive, os.getlogin())):
                    # print("PATH-->", root)
                    if not files and not dirnames:
                        print("EMPTY FILE-->", root)
                        log.write("{}\n".format(root.encode("utf-8")))
                        emptyFileCount = emptyFileCount + 1
                    totalFileCount = totalFileCount + 1
            else:
                print("Downloads Not Found")

            print("Files processed... {}".format(totalFileCount))

            if os.path.exists("{}:\\Users\\{}\\Music".format(drive, os.getlogin())) is True:
                print("Music Found")
                for root, dirnames, files in os.walk("{}:\\Users\\{}\\Music".format(drive, os.getlogin())):
                    # print("PATH-->", root)
                    if not files and not dirnames:
                        print("EMPTY FILE-->", root)
                        log.write("{}\n".format(root.encode("utf-8")))
                        emptyFileCount = emptyFileCount + 1
                    totalFileCount = totalFileCount + 1
            else:
                print("Music Not Found")

            print("Files processed... {}".format(totalFileCount))

            if os.path.exists("{}:\\Users\\{}\\Pictures".format(drive, os.getlogin())) is True:
                print("Pictures Found")
                for root, dirnames, files in os.walk("{}:\\Users\\{}\\Pictures".format(drive, os.getlogin())):
                    # print("PATH-->", root)
                    if not files and not dirnames:
                        print("EMPTY FILE-->", root)
                        log.write("{}\n".format(root.encode("utf-8")))
                        emptyFileCount = emptyFileCount + 1
                    totalFileCount = totalFileCount + 1
            else:
                print("Pictures Not Found")

            print("Files processed... {}".format(totalFileCount))

            if os.path.exists("{}:\\Users\\{}\\Videos".format(drive, os.getlogin())) is True:
                print("Documents Found")
                for root, dirnames, files in os.walk("{}:\\Users\\{}\\Videos".format(drive, os.getlogin())):
                    # print("PATH-->", root)
                    if not files and not dirnames:
                        print("EMPTY FILE-->", root)
                        log.write("{}\n".format(root.encode("utf-8")))
                        emptyFileCount = emptyFileCount + 1
                    totalFileCount = totalFileCount + 1
            else:
                print("Documents Not Found")

            print("Files processed... {}".format(totalFileCount))
        else:
            print("No Users File Found")

        for root, dirnames, files in os.walk("{}:\\".format(drive)):
            # print("PATH-->", root)
            for i in range(len(ignore)):
                if root.find(ignore[i]) == -1:
                    if i == len(ignore) - 1:
                        if not files and not dirnames:
                            print("EMPTY FILE-->", root)
                            log.write("{}\n".format(root.encode("utf-8")))
                            emptyFileCount = emptyFileCount + 1

                        if totalFileCount % 1000 == 0:
                            # os.system('cls')
                            print("Files processed... {}".format(totalFileCount), end='\r')

                        totalFileCount = totalFileCount + 1
                else:
                    break

        log.write("TOTAL FILES--> {}\n".format(totalFileCount))
        log.write("EMPTY FILES--> {}\n".format(emptyFileCount))
        log.write("{:.2f}% of your files are empty\n".format((float(emptyFileCount) / float(totalFileCount)) * 100))

    print("Files processed... {}".format(totalFileCount))
    print()
    print("TOTAL FILES-->", totalFileCount)
    print("EMPTY FILES-->", emptyFileCount)
    print("{:.2f}% of your files are empty".format((float(emptyFileCount) / float(totalFileCount)) * 100))

    end = input("Press enter to close...")

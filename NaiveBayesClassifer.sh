import sys, os, os.path

if __name__ == "__main__":
    from NaiveBayesClassifer import run_train_test
    testingdata = sys.argv[1]
    traindata = sys.argv[2]
    run_train_test(testingdata,traindata)

    
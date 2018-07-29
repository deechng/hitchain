import os
import subprocess

def runSonarScanner(repo_path):
    sonar_scanner_command = 'sonar-scanner'
    if not os.path.isdir(repo_path):
        print("Invalid path!")
    else:
        os.chdir(repo_path)
        print('Sonar Scanner Begin.')
        proc = subprocess.call(sonar_scanner_command, shell=True)
        # proc = subprocess.Popen(sonar_scanner_command, shell=True, stdout=subprocess.PIPE)
        # proc.wait()
        # logs = proc.stdout.read()
        print('Sonar Scanner End.')

def runSonarScannerC(repo_path):
    sonar_scanner_command = 'sonar-scanner'
    cpp_check_command = "cppcheck -j 1 --enable=all --xml ./src/* 1>cppcheck-result-1.xml 2>&1"
    if not os.path.isdir(repo_path):
        print("Invalid path!")
    else:
        os.chdir(repo_path)
        print('Sonar Scanner Begin.')

        subprocess.call(cpp_check_command,shell=True)
        subprocess.call(sonar_scanner_command, shell=True)
        # proc = subprocess.Popen(sonar_scanner_command, shell=True, stdout=subprocess.PIPE)
        # proc.wait()
        # logs = proc.stdout.read()
        print('Sonar Scanner End.')



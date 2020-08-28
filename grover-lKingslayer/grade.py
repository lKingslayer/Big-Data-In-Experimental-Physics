#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, os, subprocess, time, shutil, json

testcases = [
    ('data/oracle_1.py', 'data/1.ans'),
    ('data/oracle_2.py', 'data/2.ans'),
    ('data/oracle_3.py', 'data/3.ans'),
    ('data/oracle_4.py', 'data/4.ans'),
    ('data/oracle_5.py', 'data/5.ans'),
    ('data/oracle_6.py', 'data/6.ans'),
    ('data/oracle_7.py', 'data/7.ans'),
    ('data/oracle_8.py', 'data/8.ans')
]

if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Please use python3")
        exit(1)

    program_file = 'grover.py'
    
    if not os.path.isfile(program_file):
        print('File {} not present!'.format(program_file))
        exit(1)

    success_count = 0
    dump_error = []

    for input, output in testcases:
        # remove the output file
        test_filename = 'grade.out'
        try:
            os.remove(test_filename)
            shutil.rmtree('__pycache__')
        except:
            pass
        shutil.copy(input, 'oracle.py')
        p = subprocess.Popen([sys.executable, program_file], stdout=open(test_filename,'w'), stderr=open(os.devnull,'w'))
        message = ''
        success = True
        start_time = time.time()
        end_time = start_time
        while p.poll() is None:
            if time.time() - start_time > 1:
                p.terminate()
                message = 'Time limit exceeded'
                success = False
                dump_error.append({input: message})
        else:
            if not os.path.isfile(test_filename):
                message = 'No output file found'
                success = False
                dump_error.append({input: message})
            else:
                std = open(output, 'r').read().strip()
                ans = open(test_filename, 'r').read().strip()
                if std != ans:
                    message = 'expect \'{}\', but get \'{}\''.format(std, ans)
                    success = False
                    dump_error.append({input: message})
                else:
                    end_time = time.time()
        if success:
            success_count += 1
            if os.isatty(1):
                print('Testcase {}: PASS, time {:.3f}s'.format(input,
                    end_time - start_time))
        else:
            if os.isatty(1):
                print('Testcase {}: {}'.format(input, message))
        
        
    grade = int(100.0 * success_count / len(testcases))
    
    if os.isatty(1):
        print('Total Points: {}/100'.format(grade))
    else:
        if len(dump_error) == 0:
            print(json.dumps({'grade': grade}))
        else:
            print(json.dumps({'grade': grade, 'error': dump_error}))

    os.remove(test_filename)
    shutil.rmtree('__pycache__')
    shutil.copy('data/oracle_1.py', 'oracle.py')

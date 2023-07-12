remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/bllgl01/home.git/'
student-00-fa0adfa0a1a4@linux-instance:~/home$ git push origin main
Username for 'https://github.com': bllgl01
Password for 'https://bllgl01@github.com':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 330 bytes | 330.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/bllgl01/home.git
   5c5dd7b..29cafd8  main -> main
student-00-fa0adfa0a1a4@linux-instance:~/home$ nano example.py
student-00-fa0adfa0a1a4@linux-instance:~/home$ git add example.p
fatal: pathspec 'example.p' did not match any files
student-00-fa0adfa0a1a4@linux-instance:~/home$ git add example.py
student-00-fa0adfa0a1a4@linux-instance:~/home$ git add example.py
student-00-fa0adfa0a1a4@linux-instance:~/home$ git commit
Aborting commit due to empty commit message.
student-00-fa0adfa0a1a4@linux-instance:~/home$ nano example.py
  GNU nano 5.4                           example.py
def git_opeation():
 print("I am adding example.py file to the remote repository.")
git_opeation()

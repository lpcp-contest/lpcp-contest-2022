# LP/CP Programming Contest 2022

The traditional LP/CP Programming Contest will be run **on site** during ICLP 2022.
It will be a night event, it will start on 2 August at 20:00 and it will end on 3 August at 08:00.
Participants will work from their hotel rooms (or from their favourite location), and at least one of them must be registered and present at the conference.
We will provide remote support for all of the twelve hours, while participants can choose how much time to dedicate to the contest.

Winners will be announced on 3 August during the first FLoC Olympic Game session (16:00-17:30).
Members of the winning team will receive FLoC Olympic Game medals.

The contest combines some features of Prolog programming contest, Answer Set Programming (ASP) Model and Solve contest, and Constraint Programming (CP) Model and Solve contest.
A variety of systems can be used in the competition, and as in the previous edition participants are not constrained to use a single system and can also combine declarative and imperative programming languages.
Submitted solutions are expected to have a declarative predominant core.

Input and output format of problems will be provided according to some easy-to-parse representation, and similarly output must be provided according to some easy-to-write format.
(Please, have a look at the [previous edition](https://github.com/alviano/lpcp-contest-2021) of the contest to get an idea of the input and output format.)

**Checkers will be provided to participants** via a Python client, so to ease the identification of bugs thanks to textual representations of testcases and solutions.
The Python client can be downloaded from this repository, and it must be modified to specify the URL of the backend server (to be given during the contest).

Each team consists of three participants.
Submitted solutions will be tested on additional instances, and are expected to terminate in 10 minutes on an 11th Gen Intel(R) Core(TM) i5-11400 @ 2.60GHz.
Memory usage will be limited to 6 GiB.
Limits on the input (eg. range of variables) will be given for each problem.


## Systems

The following systems can be used 

* SWI-Prolog: http://www.swi-prolog.org
* GNU Prolog: http://gprolog.org
* Ciao Prolog: http://ciao-lang.org
* ECLiPSe Prolog: http://eclipseclp.org
* XSB Prolog: http://xsb.sourceforge.net
* Potassco: http://potassco.sourceforge.net
* Picat: http://picat-lang.org
* MiniZinc: http://www.minizinc.org
* IDP: https://dtai.cs.kuleuven.be/software/idp

A Docker image where all systems are installed in is available from the previous edition of the contest. Details on the installation and usage of the Docker image can be found here.
It is suggested to try your systems of choice within the Docker image, and write us an email in case some wanted feature or system is missing.

Other systems can be used as well, among them

* z3: https://github.com/Z3Prover/z3

We may ask some help to run your solutions.


## Scoring

Participants will be ranked by **number of solved instances**.
A solution is valid as soon as it does not produce wrong answers for the tested instances (timeouts and memouts are OK, but will not contribute any point).
Participants will receive feedback on the number of solved instances and on errors of their submissions.
As a general suggestion, **submit solutions as soon as you have them**.


## Registration

Send an email to mario.alviano@unical.it with subject **LP/CP Programming Contest 2022 - Registration** and the following content:

* Team name;
* List of participants and affiliations;
* One or more emails to receive feedback.

A confirmation email will be sent to you as soon as possible (usually within 24 hours).



## Submission

Via EasyChair at the following URL: **to be announced**

For each problem you solved, submit a ZIP archive with all files needed to run your solution.
The title must obey the following format:

```
team-name:problem-number
```

A good entry-point is a script like `solve.sh` reading input instances from STDIN and producing output on STDOUT.
If you opt for a different entry-point or different usage, provide instructions on how to execute your solution in the abstract.

Keywords are not important, but you have to provide at least three of them. Use the following:

```
one
two
three
```


## Checkers

The Python client to invoke the remote checkers expects two command-line parameters, namely the problem-ID and the instance-ID.
The solution to be checked is read from standard input.

Let us consider [problem-2](https://github.com/alviano/lpcp-contest-2021/tree/main/problem-2) of the previous edition, and its first instance (ie. [instance-1](https://github.com/alviano/lpcp-contest-2021/blob/main/problem-2/instance.1.in)).
If the solution to be checked is stored in file `instance.1.out`, the checker can be run as follows:
```bash
$ ./checker.py 2 1 <instance.1.out
#### STEP 0 ####
 1  2  2  1  3 
 1  2  4  3  4 
 4  1  4  5  4 
 3  2  3  3  4 
 5  5  5  5  4 

#### STEP 1 ####
 1  2  2  1  3 
[1] 2  4  3  4 
 4 [1] 4  5  4 
 3  2  3  3  4 
 5  5  5  5  4 

#### STEP 2 ####
 1  2 [2] 1  3 
 . [2] 4  3  4 
 4  .  4  5  4 
 3  2  3  3  4 
 5  5  5  5  4 

#### STEP 3 ####
 1 [2] .  1  3 
 . [.] 4  3  4 
 4 [.] 4  5  4 
 3 [2] 3  3  4 
 5  5  5  5  4 

#### STEP 4 ####
 1  .  .  1  3 
 .  .  4  3  4 
[4][.][4] 5  4 
 3  .  3  3  4 
 5  5  5  5  4 

#### STEP 5 ####
 1  .  .  1  3 
 .  .  4  3  4 
 .  .  .  5  4 
[3][.][3][3] 4 
 5  5  5  5  4 

#### STEP 6 ####
 1  .  .  1  3 
 .  .  4  3  4 
 .  .  . [5] 4 
 .  .  . [.] 4 
 5  5  5 [5] 4 

#### STEP 7 ####
[1][.][.][1] 3 
 .  .  4  3  4 
 .  .  .  .  4 
 .  .  .  .  4 
 5  5  5  .  4 

#### STEP 8 ####
 .  .  .  .  3 
 .  . [4] 3  4 
 .  .  . [.] 4 
 .  .  .  . [4]
 5  5  5  .  4 

#### STEP 9 ####
 .  .  .  .  3 
 .  .  .  3  4 
 .  .  .  .  4 
 .  .  .  .  . 
[5][5][5] .  4 

#### STEP 10 ####
 .  .  .  . [3]
 .  .  . [3] 4 
 .  .  .  .  4 
 .  .  .  .  . 
 .  .  .  .  4 

#### STEP 11 ####
 .  .  .  .  . 
 .  .  .  . [4]
 .  .  .  . [4]
 .  .  .  . [.]
 .  .  .  . [4]

CORRECT!
```

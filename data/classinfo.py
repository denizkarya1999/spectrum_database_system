import os
syllabus = '''
        General Course Information: COSC 146.2 (FA-19)
        Course Number: Course: COSC 146 Section: 2 CRN: 14527 Title: Applied Programming & Scripting Semester: FA-19 Credits: 3
        Prerequisites: none
        Textbooks: None required. Recommended Reading: Charles Severance, Python for Everybody, free e-book (2016) Allen Downey, Think Python, Green Tea Press, free e-book (2015)
        When and Where: MON/WED 17:30 – 19:10 / Pray-Harrold 521
        Final Exam: 2019-12-16 (MON) 17:30-19:00    room Pray-Harrold 521
        Instructor: Philip L. Francis, III
        Contact Info: Office: Pray-Harrold 511-F Phone: +1.734.487.1580 Department: +1.734.487.1063 Email: philip.francis@emich.edu Homepage: http://emunix.emich.edu/~francisi/emich Title: Lecturer, Dept. of Computer Science
        Office Hours: MON-THU 17:00-17:30, 19:10 – 19:40 (other times by appointment).
        Course Description: Introduction to computer programming for the non-major. Basic programming constructs; variables, functions, assignment, control structures (conditionals, looping), primitive types and aggregate types. Boolean and logic operations (and, or, not, xor). Scripting for automating system tasks. Techniques for debugging.
        Grading:
        Scale: Percentage is [earned points/max points possible]: 93+ A, 90+ A-, 87+ B+, 83+ B, 80+ B-, 77+ C+, 73+ C, 70+ C-, 67+ D+, 63+ D, 60+ D-, Below 60 E.
         You are guaranteed the above scale.  Grades may be curved at the end of the semester (depending on class performance). The curve can only help.
        Incomplete: Talk to me as soon as you think you need an incomplete. Incomplete is granted per University regulations.
        Grade Calculation:
         30 % Programming Projects (8)  25 % Quizzes (8)  20 % Labs (12)  20 % Exams (2; 10 % each)   5 % Attendance and Participation (2.5 % each)
        Makeups: There are no makeups. Exceptions are for documented medical reasons or other University sanctioned reasons. If you talk to me in advance of an exam date, I might be able to accommodate you and schedule an alternate date.
        Submission Policy: Unless otherwise specified, the following actions must be taken for proper grading of projects, assignments, etc.:  Projects upload to Canvas before time deadline on due date.  You may submit to Canvas more than once, though I only look at the most recent submission (unless you notify me to look at earlier versions).  Be prepared to discuss your code in class.  If the project requirements require your code to be residing on a server as part of the project, it must be there at the time it is due and remain untouched for the duration of the grading period.
        Late Policy: There is a minimum 15 % (of maximum possible points) penalty for late assignments. Each day of lateness carries an extra 15 % off (excluding weekends). Once graded material has been returned to the class, late work will no longer be accepted. Exceptions will not be made for mistakes in the submission process. It is considered late if you have to make another submission after the due time due to lack of planning.
        Policies:
        Email: The following should be observed with email communication:  Use only a valid emich email address.  Email subject field must communicate section & topic – e.g.: COSC 146.03 : question re project 1.
        Lab Rules: There are at least two (2) sets of rules that you should be aware of that pertain to lab rules.  Computer Science Lab Policies: http://emunix.emich.edu/~francisi/emich/lab_policies.pdf  College of Arts and Sciences Lab Policies: http://it.emich.edu/service/labs/labpolicies.cfm
        Attendance: Attendance is required and strongly encouraged.
        Weather: The EMU weather policy may be found here: http://www.emich.edu/univcomm/weatherpolicy.php
        If class session or laboratory is canceled due to bad weather or instructor absence, students are still responsible for all the readings and assignments listed on the syllabus. In the event that bad weather circumstances arise (e.g., a snow storm exam day), please remember that I am fair.
        Religious Holidays: Both Eastern Michigan University and I recognize the right of students to observe religious holidays without penalty to the student. Per Board of Regents Policy 6.2.5, I must make accommodations for students who miss class or exams due to religious holidays.  I wholeheartedly and respectfully accommodate such needs.
        Students must provide advance notice in writing to the instructor to be allowed to make up work (including examinations) that are missed as a result of absence from class due to observance of religious holidays.
        Policies (continued):
        Conduct: Any successful learning experience requires mutual respect. Neither instructor nor student should be subject to behavior that is rude, disruptive, intimidating, or demeaning. Views may differ on what counts as rudeness or courtesy. If you are not sure what constitutes good conduct in this classroom, ask the instructor. The instructor has primary responsibility for and control over classroom behavior and maintenance of academic integrity.
        Plagiarism: Plagiarism occurs when a writer deliberately passes off another's words or ideas without acknowledging their source. For example, turning another's work as your own is plagiarism. If you plagiarize in this class, you will likely fail the assignment on which you are working and your case may be passed to the university for additional disciplinary action. Because of the design and nature of this course, it will take as much (or more) work for you to plagiarize it than it will to actually complete the work of the class.
        Plagiarism is different from misuse of sources, occasions when a writer does not properly cite a source, misuses quotations, includes too much of an original source in a paraphrase or summary, or commits similar unintentional violations of academic protocol. If you misuse sources, we will work together on appropriately incorporating and/or citing the sources. Note that some audiences/instructors will consider misuse of sources to be plagiarism; for this reason, it is extreme important for you to identify the conventions associated with source use and citations in any class (or writing situation).
        Polices (continued):
        FERPA: The Family Educational Rights and Privacy Act (FERPA) is a federal law designated to protect the privacy of a student’s education records and academic work. The law applies to all schools and universities which receive funds under an applicable program of the U.S. Department of Education and is applicable to students at EMU. All files, records, and academic work completed within this course are considered educational records and are protected under FERPA. It is your right as a student in this course to expect that any materials you submit in this course as well as your name and other identifying information will not be viewable by guests or other individuals permitted access to the course. The exception will be only when you have given explicit, written, signed consent. Verbal consent or email is insufficient. For further information on FERPA, contact the Ombudsman.
        Disability Needs: It is my goal that this class be an accessible and welcoming experience for all students, including those with disabilities that may affect their learning in this class. 
        Accommodations are made legally for students with documented needs. Please exercise discretion and respect for the privacy of students with such needs.
        EMU Board of Regents Policy 8.3 requires that anyone wishing accommodation for a disability first registers with the Disability Resource Center (DRC) in 240 EMU Student Center, telephone +1.734.487.2470. Students with disabilities are encouraged to register with the DRC promptly as you will only be accommodated from the date you register. No retroactive accommodations are possible.
        '''

print(syllabus)
os.system('adminterminal.py')
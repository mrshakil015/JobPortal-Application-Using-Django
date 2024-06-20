# JobPortal-Application-Using-Django

## Models:
+ CustomUserModel

## Custom User Model:
+ Username
+ email
+ password
+ UserType (Employer, Seeker)

## Employer Model:
+ Company Name
+ Company Address
+ CompanyDescription
+ Mobile
+ CompanyLogo

## Seeker Model:
+ Name
+ Address
+ Mobile
+ DateOfBirth
+ ProfileImg
+ Resume
+ LastDegree
+ LinkedIn
+ GitHub

## Qualification Model:
+ DegreeName
+ InstituteName
+ Department
+ PassingYear
+ Grade

## Work Experience Model:
+ Designation
+ InstituteName
+ Duration

## Job Info Model:
+ JobTitle
+ CompanyName (Already in Employer Model)
+ Address (Already in Employer Model)
+ CompanyDescription (Already in Employer Model)
+ JobDescription
+ Qualification
+ Salary
+ Deadline
+ Designation
+ Experience
+ TotalVacancy
+ JobType(FullTime,PartTime,Contractual,Internship,Freelance)
+ ExperienceLevel(Begineer,MidLevel,Experienced,TopLevel)

## Job Applicant Model:
+ Applicant
+ Job
+ Skills
+ Status

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
+ CompanyName
+ Address
+ CompanyDescription
+ JobDescription
+ Qualification
+ Salary
+ Deadline
+ Designation
+ Experience

+TotalVacancy
+ JobType(FullTime,PartTime,Contractual,Internship,Freelance)
+ ExperienceLevel(Begineer,MidLevel,Experienced,TopLevel)

## Job Applicant Model:
+ Applicant
+ Job
+ Skills
+ Status

const fs = require('fs');

const portfolioData = {};

const personalInfo = {
    name: "Kaleb Coleman",
    email: "kac965@nau.edu",
    phone: "480-359-8122",
    location: "NAU, USA",
    linkedin: "https://www.linkedin.com/in/kaleb-coleman-a1807a284/",
    github: "https://github.com/kalebcoleman"
};

portfolioData.personalInfo = personalInfo;

const technicalSkills = [
    "Data Visualization", "Machine learning", "Deep learning", 
    "Computer vision", "Large language models", "Web Development",
    "TensorFlow", "Langchain", "Matplotlib", "Azure", 
    "AWS", "GitHub", "Python", "SQL", "Pandas", 
    "React", "Django", "Rust"
];

const softSkills = [
    "Communication", "Leadership", "Problem solving", 
    "Project Management", "Time Management", "Continuous Learning"
];

const skills = technicalSkills.concat(softSkills).sort();
portfolioData.skills = skills;

const educationPrototype = {
    degree: "degree",
    institution: "institution",
    fieldOfStudy: "Data Science",
    graduationYear: "2026",
}

const educationSection = [
    {
        degree: "Data Science (Major), Cyber Security (Minor)",
        institution: "Northern Arizona University",
        fieldOfStudy: "Data Science",
        graduationYear: "Current"
    },
    {
        degree: "SQL & Python Trainee",
        institution: "The Global Tech Experience",
        fieldOfStudy: "Data Science",
        graduationYear: "August 2023"
    },
    {
        degree: "Various Positions",
        institution: "McDonald's, Walmart, Smash Burger",
        fieldOfStudy: "Various",
        graduationYear: "Before College"
    }
];

portfolioData.education = educationSection;

const projectPrototype = {
    name: "project name",
    description: "project description",
    technologies: ['tech1', 'tech2', 'tech3']
};

const projectSection = [
    {
        name: "The Recording Academy Grammy.com Project",
        description: "Conducted data analysis and visualization of website data for grammy.com.",
        technologies: ["Data Analysis", "Visualization", "Business Goals"]
    },
    {
        name: "My AI Bot",
        description: "An AI-powered voice command assistant using MERN stack and Langchain.",
        technologies: ["MongoDB", "Express.js", "React.js", "Node.js", "Langchain"]
    }
];

portfolioData.projects = projectSection;

const experiencePrototype = {
    company: "company title",
    position: "position title",
    responsibilities: "responsibilities",
    startDate: "start date",
    endDate: "end date"
};  

const experienceSection = [
    {
        company: "Northern Arizona University",
        position: "Data Science Student",
        responsibilities: "Studying Data Science and Cyber Security",
        startDate: "2021",
        endDate: "2026"
    },
    {
        company: "The Global Tech Experience",
        position: "SQL & Python Trainee",
        responsibilities: "Training in SQL and Python",
        startDate: "May 2023",
        endDate: "August 2023"
    },
    {
        company: "Walmart, McDonald's, Smash Burger",
        position: "Various Positions",
        responsibilities: "Various responsibilities before college",
        startDate: "Before College",
        endDate: "2021"
    }
];

portfolioData.experience = experienceSection;

const mediaLinks = [
    { name: "LinkedIn", url: "https://www.linkedin.com/in/kaleb-coleman-a1807a284/", isActive: true },
    { name: "Facebook", url: "profile URL", isActive: false },
    { name: "Instagram", url: "profile URL", isActive: false },
    { name: "Resume", url: "https://drive.google.com/file/d/1aAZT_85vPYvmxLt9waOl3y6rrM4nyoGp/view?usp=drive_link", isActive: true },
    { name: "AI Bot", url: "https://happy-grass-084f3eb10.5.azurestaticapps.net/", isActive: true },
    { name: "GitHub", url: "https://github.com/kalebcoleman", isActive: true }
];

const filteredLinks = mediaLinks.filter(link => link.isActive);
portfolioData.mediaLinks = filteredLinks

fs.writeFile('portfolioData.json', JSON.stringify(portfolioData, null, 2), (err) => {
    if (err) throw err;
    console.log('The file saved!');
});

# Nlp-bioclassification
This project is a text mining project. A list of 2000 bios is to be scanned and the place where the person studied is to be mined.
for example:

The bio = 

'Ms. Sonya Brown serves as a General Partner at Norwest Venture Partners. She brings to Norwest more than a decade of investment experience. Based in Norwest’s Palo Alto office, Sonya is focused on investing across a wide range of sectors including information services, software, business services, financial services and consumer. Her current investments include Bailey 44, Kendra Scott Design, My Alarm Center, PCA Skin, and The Learning Experience. Sonya is also a board observer at Madison Reed. Sonya was previously at Summit Partners, a private equity firm with over $11 billion under management, where she worked for nine years in the Boston office and was responsible for leading the firm’s Consumer and Internet Industry Group in North America. Sonya was engaged in all aspects of the deal process including deal sourcing, due diligence, deal negotiations and board representation. Her most recent and past board directorships and investments include Aramsco, Airborne Health, Central Security Group, Physicians Formula Holdings (Nasdaq: FACE), Snap Fitness and Sparta Systems. Prior to joining Summit, Sonya was a founder and General Partner of iXL Ventures in 1999, where she oversaw the funding and growth of numerous technology and Internet companies. In addition, she was Vice President of Corporate Development for the parent company iXL Enterprises, Inc., one of the largest global web development companies at that time. Sonya began her career in the investment banking division of Bear Stearns where she worked on numerous consumer and media transactions. Sonya holds a bachelor of science degree from Northwestern University and an MBA from Harvard Business School. In addition, she is a Chartered Financial Analyst.' 


The output should be : Bachelors Uni: Northwestern University, Bachelors field: science, Masters education: MBA, Masters Uni: Harvard Business school. (also output extra education if any)



The code uses nltk and Spacey to go through each of the sentences and break it down. The comments in the code are sufficient to understand the code. 

The Bio with extracted data is there at this link: https://drive.google.com/file/d/1zC8xm5YtPB-Mj8BRlzUU_u7xEFzGcp1F/view?usp=sharing

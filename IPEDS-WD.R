require(dplyr)

unitid.qid = read.csv('unitid-qid.csv')
unitid.qid$item = sub('http://www.wikidata.org/entity/','',unitid.qid$item)
colnames(unitid.qid) = c('qid','unitid')

carnegie.qid = read.csv('carnegie-wikidata-crosswalk.csv')

schools = read.csv('carnegieBasic.csv') %>%
  select(unitid, Undergraduate.Program, Graduate.Program,
         Enrollment.Profile, Undergraduate.Profile, Size...Setting, Basic)

crosswalked = merge(schools, unitid.qid, by.x = 'unitid', by.y = 'unitid')

#basic = merge(crosswalked, 
#              carnegie.qid %>% filter(carnegieClassificationType == 'Basic'),
#              by.x = 'Basic', by.y = 'carnegieClassification') %>%
#  select(schoolQid = qid, carnegieQid = wikidataQid)
#cat(paste(basic$schoolQid, 'P2643', basic$carnegieQid, 'S248','Q4223026',sep = '\t'), sep = '\n')

#grad.program = merge(crosswalked, 
#                     carnegie.qid %>% filter(carnegieClassificationType == 'Graduate Instructional Program'),
#                     by.x = 'Graduate.Program', by.y = 'carnegieClassification') %>%
#  select(schoolQid = qid, carnegieQid = wikidataQid)
#cat(paste(grad.program$schoolQid, 'P2643', grad.program$carnegieQid, 'S248','Q4223026',sep = '\t'), sep = '\n')

size.setting = merge(crosswalked, 
                     carnegie.qid %>% filter(carnegieClassificationType == 'Size and Setting'),
                     by.x = 'Size...Setting', by.y = 'carnegieClassification') %>%
  select(schoolQid = qid, carnegieQid = wikidataQid)
cat(paste(size.setting$schoolQid, 'P2643', size.setting$carnegieQid, 'S248','Q4223026',sep = '\t'), sep = '\n')
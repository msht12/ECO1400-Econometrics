import pandas as pd
import pyreadstat

parent_vars = ['pid',
                   'fid',
                   'cid',
                   'provid',
                   'countyid',
                   'urban',
                   'intyear',
                   'genderm',
                   'birthyr',
                   'age',
                   'ccp',
                   'ccp_year',
                   'marital',
                   'first_marriage',
                   'year_married',
                   'year_divorced',
                   'salary',
                   'educ_degree',
                   'educ_years',
                   'life_rating']

child_vars = ['pid',
                   'fid',
                   'cid',
                   'provid',
                   'countyid',
                   'urban',
                   'intyear',
                   'genderm',
                   'birthyr',
                   'age',
                   'b_feed_mon',
                   'board_school',
                   'verbal',
                   'math',
                 'fam_member_tut_hrs1',
                 'fam_member_tut_hrs2',
                 'fam_member_tut_hrs3',
                 'fam_member_tut_hrs4',
                 'fam_member_tut_hrs5',
                 'pid_f',
                 'pid_m',
                 'educ_years']

# Parent data
dfCFPS2018adult, meta = pyreadstat.read_dta("~/ecfps2018person_202012.dta")
dfCFPS2016adult, meta = pyreadstat.read_dta("~/ecfps2016adult_201906.dta")
dfCFPS2014adult, meta = pyreadstat.read_dta("~/ecfps2014adult_201906.dta")
dfCFPS2012adult, meta = pyreadstat.read_dta("~/ecfps2012adult_201906.dta")
dfCFPS2010adult, meta = pyreadstat.read_dta("~/ecfps2010adult_202008.dta")

# filter out parent variables to only the ones we need
# We will rename the columns based on 2010
# 2018
dfCFPS2018adult.rename(columns = {'pid':'pid',
                                  'fid18':'fid',
                                  'cid18':'cid',
                                  'provcd18':'provid',
                                  'countyid18':'countyid',
                                  'urban18':'urban',
                                  'cyear':'intyear',
                                  'gender':'genderm',
                                  'qa001y':'birthyr',
                                  'age':'age',
                                  'qn4001':'ccp',
                                  'qn402':'ccp_year',
                                  'qea0':'marital',
                                  'qea2071':'first_marriage',
                                  'qea205y':'year_married',
                                  'qea208y':'year_divorced',
                                  'qg11':'salary',
                                  'w01':'educ_degree',
                                  'cfps2018eduy_im':'educ_years',
                                  'qn12012':'life_rating'}, inplace = True)
dfCFPS2018adultfiltered = dfCFPS2018adult[parent_vars]
#print(dfCFPS2018adultfiltered)

# 2016
dfCFPS2016adult.rename(columns = {'pid':'pid',
                                  'fid16':'fid',
                                  'cid16':'cid',
                                  'provcd16':'provid',
                                  'countyid16':'countyid',
                                  'urban16':'urban',
                                  'cyear':'intyear',
                                  'cfps_gender':'genderm',
                                  'cfps_birthy':'birthyr',
                                  'cfps_age':'age',
                                  'cfps_hk':'hukou',
                                  'qn4001':'ccp',
                                  'qn402':'ccp_year',
                                  'qea0':'marital',
                                  'qea2071':'first_marriage',
                                  'qea205y':'year_married',
                                  'qea208y':'year_divorced',
                                  'qg11':'salary',
                                  'cfps2016edu':'educ_degree',
                                  'cfps2016eduy_im':'educ_years',
                                  'qn12012':'life_rating'}, inplace = True)
dfCFPS2016adultfiltered = dfCFPS2016adult[parent_vars]
#print(dfCFPS2016adultfiltered)

# 2014
dfCFPS2014adult.rename(columns = {'pid':'pid',
                                  'fid14':'fid',
                                  'cid14':'cid',
                                  'provcd14':'provid',
                                  'countyid14':'countyid',
                                  'urban14':'urban',
                                  'cyear':'intyear',
                                  'cfps_gender':'genderm',
                                  'cfps_birthy':'birthyr',
                                  'cfps2014_age':'age',
                                  'pn401a':'ccp',
                                  'qn402':'ccp_year',
                                  'qea0':'marital',
                                  'qea2071':'first_marriage',
                                  'qea205y':'year_married',
                                  'qea208y':'year_divorced',
                                  'qg11':'salary',
                                  'cfps2014edu':'educ_degree',
                                  'cfps2014eduy':'educ_years',
                                  'qn12012':'life_rating'}, inplace = True)
dfCFPS2014adultfiltered = dfCFPS2014adult[parent_vars]

# 2012
dfCFPS2012adult.rename(columns = {'pid':'pid',
                                  'fid12':'fid',
                                  'cid':'cid',
                                  'provcd':'provid',
                                  'countyid':'countyid',
                                  'urban12':'urban',
                                  'cyear':'intyear',
                                  'cfps2012_gender':'genderm',
                                  'cfps2012_birthy':'birthyr',
                                  'cfps2012_age':'age',
                                  'sn401':'ccp',
                                  'qn402':'ccp_year',
                                  'qe104':'marital',
                                  'qe210':'first_marriage',
                                  'qec105y':'year_married',
                                  'qe306y':'year_divorced',
                                  'income':'salary',
                                  'edu2012':'educ_degree',
                                  'eduy2012':'educ_years',
                                  'qn12012':'life_rating'}, inplace = True)
dfCFPS2012adultfiltered = dfCFPS2012adult[parent_vars]

# 2010
dfCFPS2010adult.rename(columns = {'pid':'pid',
                                  'fid':'fid',
                                  'cid':'cid',
                                  'provcd':'provid',
                                  'countyid':'countyid',
                                  'indno':'hhcode',
                                  'urban':'urban',
                                  'cyear':'intyear',
                                  'gender':'genderm',
                                  'qa1y':'birthyr',
                                  'qa1age':'age',
                                  'qa2':'hukou',
                                  'qa7_s_1':'ccp',
                                  'qa701':'ccp_year',
                                  'qe1_best':'marital',
                                  'qe2':'first_marriage',
                                  'qe210y':'year_married',
                                  'qe402y':'year_divorced',
                                  'qk101':'salary',
                                  'cfps2010edu_best':'educ_degree',
                                  'cfps2010eduy_best':'educ_years',
                                  'qm403':'life_rating'}, inplace = True)
dfCFPS2010adultfiltered = dfCFPS2010adult[parent_vars]

# Add suffixes to each adult survey for year and a for adult
dfCFPS2018adultfiltered = dfCFPS2018adultfiltered.add_suffix('_2018')
dfCFPS2016adultfiltered = dfCFPS2016adultfiltered.add_suffix('_2016')
dfCFPS2014adultfiltered = dfCFPS2014adultfiltered.add_suffix('_2014')
dfCFPS2012adultfiltered = dfCFPS2012adultfiltered.add_suffix('_2012')
dfCFPS2010adultfiltered = dfCFPS2010adultfiltered.add_suffix('_2010')
#print(dfCFPS2018adultfiltered)

# Revert keys column back to normal
dfCFPS2018adultfiltered["pid"] = dfCFPS2018adultfiltered["pid_2018"]
dfCFPS2016adultfiltered["pid"] = dfCFPS2016adultfiltered["pid_2016"]
dfCFPS2014adultfiltered["pid"] = dfCFPS2014adultfiltered["pid_2014"]
dfCFPS2012adultfiltered["pid"] = dfCFPS2012adultfiltered["pid_2012"]
dfCFPS2010adultfiltered["pid"] = dfCFPS2010adultfiltered["pid_2010"]

alladultdata = pd.merge(dfCFPS2016adultfiltered, dfCFPS2018adultfiltered, on ='pid', how ="right")
alladultdata = pd.merge(alladultdata, dfCFPS2014adultfiltered, on ='pid', how ="right")
alladultdata = pd.merge(alladultdata, dfCFPS2012adultfiltered, on ='pid', how ="right")
alladultdata = pd.merge(alladultdata, dfCFPS2010adultfiltered, on ='pid', how ="right")

# Removing entries that don't appear in both years for adults 2016-2018
#alladultdata.dropna(subset=['pid_2010'], inplace=True)

# Split into separate dataframes
adult2018clean = alladultdata.loc[:,alladultdata.columns.map(lambda x: x.endswith('_2018'))]
adult2016clean = alladultdata.loc[:,alladultdata.columns.map(lambda x: x.endswith('_2016'))]
adult2014clean = alladultdata.loc[:,alladultdata.columns.map(lambda x: x.endswith('_2014'))]
adult2012clean = alladultdata.loc[:,alladultdata.columns.map(lambda x: x.endswith('_2012'))]
adult2010clean = alladultdata.loc[:,alladultdata.columns.map(lambda x: x.endswith('_2010'))]

# Remove the suffixes to prepare for appending
adult2018clean.columns=adult2018clean.columns.str.rstrip('_2018')
adult2016clean.columns=adult2016clean.columns.str.rstrip('_2016')
adult2014clean.columns=adult2014clean.columns.str.rstrip('_2014')
adult2012clean.columns=adult2012clean.columns.str.rstrip('_2012')
adult2010clean.columns=adult2010clean.columns.str.rstrip('_2010')

# Child data
dfCFPS2018child, meta = pyreadstat.read_dta("~/ecfps2018childproxy_202012.dta")
dfCFPS2016child, meta = pyreadstat.read_dta("~/ecfps2016child_201906.dta")
dfCFPS2014child, meta = pyreadstat.read_dta("~/ecfps2014child_201906.dta")
dfCFPS2012child, meta = pyreadstat.read_dta("~/ecfps2012child_201906.dta")
dfCFPS2010child, meta = pyreadstat.read_dta("~/ecfps2010child_201906.dta")

# Cleaning up child data var names
# 2018
dfCFPS2018child.rename(columns = {'pid':'pid',
          'fid18':'fid',
          'cid18':'cid',
          'provcd18':'provid',
          'countyid18':'countyid',
          'urban18':'urban',
          'cyear':'intyear',
          'gender_update':'genderm',
          'ibirthy_update':'birthyr',
          'age':'age',
          'wa105b':'b_feed_mon',
          'ws10':'board_school',
          'wf501':'verbal',
          'wf502':'math',
          'wf401_s_1hour':'fam_member_tut_hrs1',
          'wf401_s_2hour':'fam_member_tut_hrs2',
          'wf401_s_3hour':'fam_member_tut_hrs3',
          'wf401_s_4hour':'fam_member_tut_hrs4',
          'wf401_s_5hour':'fam_member_tut_hrs5',
          'pid_a_f':'pid_f',
          'pid_a_m':'pid_m',
          'cfps2018eduy_im':'educ_years'}, inplace = True)
dfCFPS2018childfiltered = dfCFPS2018child[child_vars]

# 2016
dfCFPS2016child.rename(columns = {'pid':'pid',
          'fid16':'fid',
          'cid16':'cid',
          'provcd16':'provid',
          'countyid16':'countyid',
          'urban16':'urban',
          'self_cyear':'intyear',
          'cfps_gender':'genderm',
          'cfps_birthy':'birthyr',
          'cfps_age':'age',
          'wa105b':'b_feed_mon',
          'ps10_b_1':'board_school',
          'wf501':'verbal',
          'wf502':'math',
          'wf401_a_1':'fam_member_tut_hrs1',
          'wf401_a_2':'fam_member_tut_hrs2',
          'wf401_a_3':'fam_member_tut_hrs3',
          'wf401_a_4':'fam_member_tut_hrs4',
          'wf401_a_5':'fam_member_tut_hrs5',                     
          'pid_f':'pid_f',
          'pid_m':'pid_m',
          'cfps2016eduy':'educ_years'}, inplace = True)
dfCFPS2016childfiltered = dfCFPS2016child[child_vars]

# 2014
dfCFPS2014child.rename(columns = {'pid':'pid',
          'fid14':'fid',
          'cid14':'cid',
          'provcd14':'provid',
          'countyid14':'countyid',
          'urban14':'urban',
          'cyear':'intyear',
          'cfps_gender':'genderm',
          'cfps_birthy':'birthyr',
          'cfps2014_age':'age',
          'wa105b':'b_feed_mon',
          'wf304s':'board_school',
          'wf501':'verbal',
          'wf502':'math',
          'wf401_a_1':'fam_member_tut_hrs1',
          'wf401_a_2':'fam_member_tut_hrs2',
          'wf401_a_3':'fam_member_tut_hrs3',
          'wf401_a_4':'fam_member_tut_hrs4',
          'wf401_a_5':'fam_member_tut_hrs5',                     
          'pid_f':'pid_f',
          'pid_m':'pid_m',
          'cfps2014eduy':'educ_years'}, inplace = True)
dfCFPS2014childfiltered = dfCFPS2014child[child_vars]

# 2012
dfCFPS2012child.rename(columns = {'pid':'pid',
          'fid12':'fid',
          'cid':'cid',
          'provcd':'provid',
          'countyid':'countyid',
          'urban12':'urban',
          'cyear':'intyear',
          'gender2':'genderm',
          'cfps2012_birthy':'birthyr',
          'cfps2012_age':'age',
          'wa105b':'b_feed_mon',
          'wf304s':'board_school',
          'wf501':'verbal',
          'wf502':'math',
          'wf401_a_1':'fam_member_tut_hrs1',
          'wf401_a_2':'fam_member_tut_hrs2',
          'wf401_a_3':'fam_member_tut_hrs3',
          'wf401_a_4':'fam_member_tut_hrs4',
          'wf401_a_5':'fam_member_tut_hrs5',                     
          'pid_f':'pid_f',
          'pid_m':'pid_m',
          'eduy2012':'educ_years'}, inplace = True)
dfCFPS2012childfiltered = dfCFPS2012child[child_vars]

# 2010
dfCFPS2010child.rename(columns = {'pid':'pid',
          'fid':'fid',
          'cid':'cid',
          'provcd':'provid',
          'countyid':'countyid',
          'urban':'urban',
          'cyear':'intyear',
          'gender':'genderm',
          'wa1y':'birthyr',
          'wa1age':'age',
          'wa105':'b_feed_mon',
          'wf304':'board_school',
          'wf501':'verbal',
          'wf502':'math',
          'wf401_a_1':'fam_member_tut_hrs1',
          'wf401_a_2':'fam_member_tut_hrs2',
          'wf401_a_3':'fam_member_tut_hrs3',
          'wf401_a_4':'fam_member_tut_hrs4',
          'wf401_a_5':'fam_member_tut_hrs5',                     
          'pid_f':'pid_f',
          'pid_m':'pid_m',
          'cfps2010eduy_best':'educ_years'}, inplace = True)
dfCFPS2010childfiltered = dfCFPS2010child[child_vars]

# Get a list of mother ids and father ids per year
# Mother ids
momids18 = dfCFPS2018childfiltered.pid_m.unique()
momids18 = list(filter(lambda x: x != 'nan' or x != -8, momids18))[1:]
momids16 = dfCFPS2016childfiltered.pid_m.unique()
momids16 = list(filter(lambda x: x != 'nan' or x != -8, momids16))[1:]
momids14 = dfCFPS2014childfiltered.pid_m.unique()
momids14 = list(filter(lambda x: x != 'nan' or x != -8, momids14))[1:]
momids12 = dfCFPS2012childfiltered.pid_m.unique()
momids12 = list(filter(lambda x: x != 'nan' or x != -8, momids12))[1:]
momids10 = dfCFPS2010childfiltered.pid_m.unique()
momids10 = list(filter(lambda x: x != 'nan' or x != -8, momids10))[1:]

# Father ids
dadids18 = dfCFPS2018childfiltered.pid_f.unique()
dadids18 = list(filter(lambda x: x != 'nan' or x != -8, dadids18))[1:]
dadids16 = dfCFPS2016childfiltered.pid_f.unique()
dadids16 = list(filter(lambda x: x != 'nan' or x != -8, dadids16))[1:]
dadids14 = dfCFPS2014childfiltered.pid_f.unique()
dadids14 = list(filter(lambda x: x != 'nan' or x != -8, dadids14))[1:]
dadids12 = dfCFPS2012childfiltered.pid_f.unique()
dadids12 = list(filter(lambda x: x != 'nan' or x != -8, dadids12))[1:]
dadids10 = dfCFPS2010childfiltered.pid_f.unique()
dadids10 = list(filter(lambda x: x != 'nan' or x != -8, dadids10))[1:]

# Split the adult dataframes based on momid and dadid from child data
# Moms
dfmoms18 = adult2018clean[adult2018clean['pid'].isin(momids18)]
dfmoms16 = adult2016clean[adult2016clean['pid'].isin(momids16)]
dfmoms14 = adult2014clean[adult2014clean['pid'].isin(momids14)]
dfmoms12 = adult2012clean[adult2018clean['pid'].isin(momids12)]
dfmoms10 = adult2010clean[adult2010clean['pid'].isin(momids10)]

# Dads
dfdads18 = adult2018clean[adult2018clean['pid'].isin(dadids18)]
dfdads16 = adult2016clean[adult2016clean['pid'].isin(dadids16)]
dfdads14 = adult2014clean[adult2014clean['pid'].isin(dadids14)]
dfdads12 = adult2012clean[adult2012clean['pid'].isin(dadids12)]
dfdads10 = adult2010clean[adult2010clean['pid'].isin(dadids10)]

# Apply _m or _d suffix to the variables to indicate mom or dad
# Moms
dfmoms18 = dfmoms18.add_suffix('_m')
dfmoms16 = dfmoms16.add_suffix('_m')
dfmoms14 = dfmoms14.add_suffix('_m')
dfmoms12 = dfmoms12.add_suffix('_m')
dfmoms10 = dfmoms10.add_suffix('_m')

# Dads
dfdads18 = dfdads18.add_suffix('_f')
dfdads16 = dfdads16.add_suffix('_f')
dfdads14 = dfdads14.add_suffix('_f')
dfdads12 = dfdads12.add_suffix('_f')
dfdads10 = dfdads10.add_suffix('_f')

# Append the mother and father dataframes to child dataframe according to momdid and dadid
fulldata18 = pd.merge(dfCFPS2018childfiltered, dfmoms18, on='pid_m')
fulldata18 = pd.merge(fulldata18, dfdads18, on ='pid_f')
fulldata18.drop(['intyear'], axis=1)
fulldata18['intyear'] = 2018
#print(fulldata18.head(10))

fulldata16 = pd.merge(dfCFPS2016childfiltered, dfmoms16, on='pid_m')
fulldata16 = pd.merge(fulldata16, dfdads16, on ='pid_f')
fulldata16.drop(['intyear'], axis=1)
fulldata16['intyear'] = 2016
#print(fulldata16.head(10))

fulldata14 = pd.merge(dfCFPS2014childfiltered, dfmoms14, on='pid_m')
fulldata14 = pd.merge(fulldata14, dfdads14, on ='pid_f')
fulldata14.drop(['intyear'], axis=1)
fulldata14['intyear'] = 2014
#print(fulldata16.head(10))

fulldata12 = pd.merge(dfCFPS2012childfiltered, dfmoms12, on='pid_m')
fulldata12 = pd.merge(fulldata12, dfdads12, on ='pid_f')
fulldata12.drop(['intyear'], axis=1)
fulldata12['intyear'] = 2012
#print(fulldata16.head(10))

fulldata10 = pd.merge(dfCFPS2010childfiltered, dfmoms10, on='pid_m')
fulldata10 = pd.merge(fulldata10, dfdads10, on ='pid_f')
fulldata10.drop(['intyear'], axis=1)
fulldata10['intyear'] = 2010
#print(fulldata16.head(10))

fulldata = pd.concat([fulldata18,fulldata16,fulldata14,fulldata12,fulldata10])
fulldata = fulldata.sort_values(by=['pid','intyear'])
#print(fulldata.head(10))

# Save the whole thing to csv
fulldata.to_csv("~/fulldata.csv")
select * from rotten_all;

# fixing typo
update rotten_all
set service = 'Netflix'
where service = 'Neflix';

# removing percent signs
update rotten_all 
set audience_score  = substring_index(audience_score,'%', 1)
where audience_score regexp '%$';

# converting percents to decimals for easier tableau analysis 
update rotten_all 
set audience_score = concat('.', audience_score)
where audience_score < 100;

update rotten_all 
set audience_score = 1
where audience_score = 100;

# separating combined genre column
update rotten_all as r
set r.genre_primary = substring_index(genre_primary,'/', 1), 
	r.genre_secondary = substring_index(genre_primary,'/', -1);

# calculating average score    
update rotten_all
set average_score = round((audience_score + critic_score) / 2, 2);
    




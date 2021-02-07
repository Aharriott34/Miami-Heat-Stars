# Comparing all the Miami Heat players who were All-Stars.
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
pd.set_option('display.max_columns', None)
heat_df = pd.read_csv('Heat All-Stars.csv')
groupby_average = heat_df.groupby(['Player']).mean()
first_column = heat_df.iloc[:,0]
years_as_star = first_column.value_counts().sort_index(ascending=True)

# Averages for each statistic.
player_names = list(groupby_average.index)
player_points = groupby_average.iloc[0:, 0]
player_assists = groupby_average.iloc[0:, 1]
player_blocks = groupby_average.iloc[0:, 2]
player_steals = groupby_average.iloc[0:, 3]
player_turnovers = groupby_average.iloc[0:, 4]
player_field_goal = groupby_average.iloc[0:, 5]
player_3_pointer = groupby_average.iloc[0:, 6]
player_free_throw = groupby_average.iloc[0:, 7]
player_rebounds = groupby_average.iloc[0:, 8]



fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

# Labels for bar graphs.
def label(stats ,figure):
    for index, value in enumerate(stats.iloc):
        figure.text(value, index, round(value, 2), ha="left", va="center")
    return(figure)

# Bar graphs showing each players average in each statistic.
fig.suptitle("Miami Heat All-Stars")
ax1.barh(player_names, player_points, align='center')
ax1.set_title("Points Per Game")
ax1.set_xlim(0, 30)
ax1.set_xticks([0, 5, 10, 15, 20, 25, 30])
ax1.set_ylabel("Players")
label(player_points, ax1)


ax2.barh(player_names, player_field_goal, align='center')
ax2.set_title("Field Goal Percentage")
ax2.set_xlim(0, 60)
ax2.set_xticks([0, 20, 40, 60, 80, 100])
ax2.set_xticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
ax2.set_ylabel("Players")
label(player_field_goal, ax2)

ax3.barh(player_names, player_3_pointer, align='center')
ax3.set_title("3-Point Percentage")
ax3.set_xticks([0, 20, 40, 60, 80, 100])
ax3.set_xticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
ax3.set_ylabel("Players")
label(player_3_pointer, ax3)

ax4.barh(player_names, player_free_throw, align='center')
ax4.set_title("Free Throw Percentage")
ax4.set_xticks([0, 20, 40, 60, 80, 100])
ax4.set_xticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
ax4.set_ylabel("Players")
label(player_free_throw, ax4)
plt.tight_layout()
plt.savefig('Miami Heat Stats 1.png', bbox_inches="tight")

fig, ((ax5, ax6), (ax7, ax8)) = plt.subplots(nrows=2, ncols=2)

fig.suptitle("Miami Heat All-Stars")
ax5.barh(player_names, player_assists)
ax5.set_title("Assists Per Game")
ax5.set_xticks([0, 2, 4, 6, 8, 10])
ax5.set_ylabel("Players")
label(player_assists, ax5)

ax6.barh(player_names, player_blocks)
ax6.set_title("Blocks Per Game")
ax6.set_xticks([0, 1, 2, 3, 4, 5])
ax6.set_ylabel("Players")
label(player_blocks, ax6)

ax7.barh(player_names, player_steals)
ax7.set_title("Steals Per Game")
ax7.set_xticks([0, 1, 2, 3, 4, 5])
ax7.set_ylabel("Players")
label(player_steals, ax7)

ax8.barh(player_names, player_turnovers)
ax8.set_title("Turnovers Per Game")
ax8.set_xticks([0, 1, 2, 3, 4, 5])
ax8.set_ylabel("Players")
label(player_turnovers, ax8)
plt.tight_layout()
plt.savefig('Miami Heat Stats 2.png', bbox_inches="tight")

fig, ax9 = plt.subplots()
fig.suptitle("Miami Heat All-Stars")
ax9.barh(player_names, player_rebounds)
ax9.set_title("Rebounds Per Game")
ax9.set_xticks([0,2,4,6,8,10,12])
ax9.set_ylabel('Players')
label(player_rebounds, ax9)
plt.tight_layout()
plt.savefig('Miami Heat Stats 3.png', bbox_inches="tight")

# Due to Dwyane Wade's career being long in Miami,the years have to be shortened to fit his line graph. Put on everyones for uniformity.
def short_year(old_list, new_list):
    for years in old_list:
        years = years.replace("19", "")
        years = years.replace("20", "")
        new_list.append(years)
    return new_list

# Bam Adebayo, Jimmy Butler, Goran Dragic, and Anthony Mason are excluded. Were only All-Stars for one season.
# Comparing points per game, assist per game, blocks per game, and rebounds per game throughout each players years.
chris_bosh_line_graph = heat_df.iloc[1:7]
cb_years = chris_bosh_line_graph.iloc[0: ,3]
chris_bosh_ppg = chris_bosh_line_graph['ppg']
chris_bosh_apg = chris_bosh_line_graph['apg']
chris_bosh_bpg = chris_bosh_line_graph['bpg']
chris_bosh_rpg = chris_bosh_line_graph['reb']
cb_short_years = []
short_year(cb_years, cb_short_years)

tim_hardaway_line_graph = heat_df.iloc[9:11]
th_years = tim_hardaway_line_graph.iloc[0: ,3]
tim_hardaway_ppg = tim_hardaway_line_graph['ppg']
tim_hardaway_apg = tim_hardaway_line_graph['apg']
tim_hardaway_bpg = tim_hardaway_line_graph['bpg']
tim_hardaway_rpg = tim_hardaway_line_graph['reb']
tim_hardaway_short_years = []
short_year(th_years,tim_hardaway_short_years)

lebron_line_graph = heat_df.iloc[11:15]
lebron_years = lebron_line_graph.iloc[0:, 3]
lebron_ppg = lebron_line_graph['ppg']
lebron_apg = lebron_line_graph['apg']
lebron_bpg = lebron_line_graph['bpg']
lebron_rpg = lebron_line_graph['reb']
lebron_short_years = []
short_year(lebron_years, lebron_short_years)

zo_line_graph = heat_df.iloc[16:21]
zo_years = zo_line_graph.iloc[0:, 3]
zo_ppg = zo_line_graph['ppg']
zo_apg = zo_line_graph['apg']
zo_bpg = zo_line_graph['bpg']
zo_rpg = zo_line_graph['reb']
zo_short_years = []
short_year(zo_years, zo_short_years)

shaq_line_graph = heat_df.iloc[21:24]
shaq_years = shaq_line_graph.iloc[0:, 3]
shaq_ppg = shaq_line_graph['ppg']
shaq_apg = shaq_line_graph['apg']
shaq_bpg = shaq_line_graph['bpg']
shaq_rpg = shaq_line_graph['reb']
shaq_short_years = []
short_year(shaq_years, shaq_short_years)

dwade_line_graph = heat_df.iloc[24:38]
dwade_years = dwade_line_graph.iloc[0:, 3]
dwade_ppg = dwade_line_graph['ppg']
dwade_apg = dwade_line_graph['apg']
dwade_bpg = dwade_line_graph['bpg']
dwade_reb = dwade_line_graph['reb']
dwade_years_short = []
short_year(dwade_years, dwade_years_short)
dwade_years_short.pop()
dwade_years_short.append('"19"')


fig, ((ax10, ax11), (ax12, ax13)) = plt.subplots(nrows=2, ncols=2)

# Labels for the line graph.
def label2(stats, figure):
    for index, value in enumerate(stats.iloc):
        figure.annotate(str(value), xy = (index, value), va="bottom", ha='right')

fig.suptitle("Chris Bosh")
ax10.set_title("Points Per Game")
ax10.plot(cb_short_years, chris_bosh_ppg, linestyle='dashed', marker="o")
ax10.set_xlabel("Years (2011-2016)")
ax10.set_yticks([0,5,10,15,20,25,30])
label2(chris_bosh_ppg, ax10)

ax11.set_title("Assist Per Game")
ax11.plot(cb_short_years, chris_bosh_apg, linestyle='dashed', marker="o")
ax11.set_xlabel("Years (2011-2016)")
ax11.set_yticks([0,2,4,6,8,10,12])
label2(chris_bosh_apg, ax11)

ax12.set_title("Blocks Per Game")
ax12.plot(cb_short_years, chris_bosh_bpg, linestyle='dashed', marker="o")
ax12.set_xlabel("Years (2011-2016)")
ax12.set_yticks([0,2,4,6,8,10,12])
label2(chris_bosh_bpg, ax12)

ax13.set_title("Rebounds Per Game")
ax13.plot(cb_short_years, chris_bosh_rpg, linestyle='dashed', marker="o")
ax13.set_yticks([0,2,4,6,8,10,12])
ax13.set_xlabel("Years (2011-2016)")
label2(chris_bosh_rpg, ax13)
plt.tight_layout()
plt.savefig('Chris Bosh Stats.png', bbox_inches="tight")

fig, ((ax14, ax15), (ax16, ax17)) = plt.subplots(nrows=2, ncols=2)
fig.suptitle("Tim Hardaway")

ax14.set_title("Points Per Game")
ax14.plot(tim_hardaway_short_years, tim_hardaway_ppg, linestyle='dashed', marker="o")
ax14.set_xlabel("Years (1997-1998)")
ax14.set_yticks([0,5,10,15,20,25,30])
label2(tim_hardaway_ppg, ax14)

ax15.set_title("Assist Per Game")
ax15.plot(tim_hardaway_short_years, tim_hardaway_apg, linestyle='dashed', marker="o")
ax15.set_xlabel("Years (1997-1998)")
ax15.set_yticks([0,2,4,6,8,10,12])
label2(tim_hardaway_apg, ax15)

ax16.set_title("Blocks Per Game")
ax16.plot(tim_hardaway_short_years, tim_hardaway_bpg, linestyle='dashed', marker="o")
ax16.set_xlabel("Years (1997-1998)")
ax16.set_yticks([0,2,4,6,8,10,12])
label2(tim_hardaway_bpg, ax16)

ax17.set_title("Rebounds Per Game")
ax17.plot(tim_hardaway_short_years, tim_hardaway_rpg, linestyle='dashed', marker="o")
ax17.set_xlabel("Years (1997-1998)")
ax17.set_yticks([0,2,4,6,8,10,12])
label2(tim_hardaway_rpg, ax17)
plt.tight_layout()
plt.savefig('Tim Hardaway Stats.png', bbox_inches="tight")

fig, ((ax18, ax19), (ax20, ax21)) = plt.subplots(nrows=2, ncols=2)

fig.suptitle("LeBron James")
ax18.set_title("Points Per Game")
ax18.plot(lebron_short_years, lebron_ppg, linestyle='dashed', marker="o")
ax18.set_xlabel("Years (2011-2014)")
ax18.set_yticks([0,5,10,15,20,25,30])
label2(lebron_ppg, ax18)

ax19.set_title("Assist Per Game")
ax19.plot(lebron_short_years, lebron_apg, linestyle='dashed', marker="o")
ax19.set_xlabel("Years (2011-2014)")
ax19.set_yticks([0,2,4,6,8,10,12])
label2(lebron_apg, ax19)

ax20.set_title("Blocks Per Game")
ax20.plot(lebron_short_years, lebron_bpg, linestyle='dashed', marker="o")
ax20.set_xlabel("Years (2011-2014)")
ax20.set_yticks([0,2,4,6,8,10,12])
label2(lebron_bpg, ax20)

ax21.set_title("Rebounds Per Game")
ax21.plot(lebron_short_years, lebron_rpg, linestyle='dashed', marker="o")
ax21.set_xlabel("Years (2011-2014)")
ax21.set_yticks([0,2,4,6,8,10,12])
label2(lebron_rpg, ax21)
plt.tight_layout()
plt.savefig('LeBron James Stats.png', bbox_inches="tight")

fig, ((ax22, ax23), (ax24, ax25)) = plt.subplots(nrows=2, ncols=2)

fig.suptitle("Alonzo Mourning")
ax22.set_title("Points Per Game")
ax22.plot(zo_short_years, zo_ppg, linestyle='dashed', marker="o")
ax22.set_xlabel("Years (1996-2002)")
ax22.set_yticks([0,5,10,15,20,25,30])
label2(zo_ppg, ax22)

ax23.set_title("Assist Per Game")
ax23.plot(zo_short_years, zo_apg, linestyle='dashed', marker="o")
ax23.set_xlabel("Years (1996-2002)")
ax23.set_yticks([0,2,4,6,8,10,12])
label2(zo_apg, ax23)

ax24.set_title("Blocks Per Game")
ax24.plot(zo_short_years, zo_bpg, linestyle='dashed', marker="o")
ax24.set_xlabel("Years (1996-2002)")
ax24.set_yticks([0,2,4,6,8,10,12])
label2(zo_bpg, ax24)

ax25.set_title("Rebounds Per Game")
ax25.plot(zo_short_years, zo_rpg, linestyle='dashed', marker="o")
ax25.set_xlabel("Years (1996-2002)")
ax25.set_yticks([0,2,4,6,8,10,12])
label2(zo_rpg, ax25)
plt.tight_layout()
plt.savefig('Alonzo Mourning Stats.png', bbox_inches="tight")

fig, ((ax26, ax27), (ax28, ax29)) = plt.subplots(nrows=2, ncols=2)

fig.suptitle("Shaquille O'Neal")
ax26.set_title("Points Per Game")
ax26.plot(shaq_short_years, shaq_ppg, linestyle='dashed', marker="o")
ax26.set_xlabel("Years (2005-2007)")
ax26.set_yticks([0,5,10,15,20,25,30])
label2(shaq_ppg, ax26)

ax27.set_title("Assist Per Game")
ax27.plot(shaq_short_years, shaq_apg, linestyle='dashed', marker="o")
ax27.set_xlabel("Years (2005-2007)")
ax27.set_yticks([0,2,4,6,8,10,12])
label2(shaq_apg, ax27)

ax28.set_title("Blocks Per Game")
ax28.plot(shaq_short_years, shaq_bpg, linestyle='dashed', marker="o")
ax28.set_xlabel("Years (2005-2007)")
ax28.set_yticks([0,2,4,6,8,10,12])
label2(shaq_bpg, ax28)

ax29.set_title("Rebounds Per Game")
ax29.plot(shaq_short_years, shaq_rpg, linestyle='dashed', marker="o")
ax29.set_xlabel("Years (2005-2007)")
ax29.set_yticks([0,2,4,6,8,10,12])
label2(shaq_rpg, ax29)
plt.tight_layout()
plt.savefig('Shaquille O\'Neal Stats.png', bbox_inches="tight")

fig, ((ax30, ax31), (ax32, ax33)) = plt.subplots(nrows=2, ncols=2)

fig.suptitle("Dwyane Wade")
ax30.set_title("Points Per Game")
ax30.plot(dwade_years_short, dwade_ppg, linestyle='dashed', marker="o")
ax30.set_xlabel("Years (2005-2019)")
ax30.set_yticks([0,5,10,15,20,25,30,35])
label2(dwade_ppg, ax30)

ax31.set_title("Assist Per Game")
ax31.plot(dwade_years_short, dwade_apg, linestyle='dashed', marker="o")
ax31.set_xlabel("Years (2005-2019)")
ax31.set_yticks([0,2,4,6,8,10,12])
label2(dwade_apg, ax31)

ax32.set_title("Blocks Per Game")
ax32.plot(dwade_years_short, dwade_bpg, linestyle='dashed', marker="o")
ax32.set_xlabel("Years (2005-2019)")
ax32.set_yticks([0,2,4,6,8,10,12])
label2(dwade_bpg, ax32)

ax33.set_title("Rebounds Per Game")
ax33.plot(dwade_years_short, dwade_reb, linestyle='dashed', marker="o")
ax33.set_xlabel("Years (2005-2019)")
ax33.set_yticks([0,2,4,6,8,10,12])
label2(dwade_reb, ax33)
plt.tight_layout()
plt.savefig('Dwyane Wade Stats.png', bbox_inches="tight")


plt.gcf().subplots_adjust(left=0.10)
plt.show()
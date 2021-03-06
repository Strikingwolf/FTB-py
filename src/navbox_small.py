# Created by Eli Foster
# Sub-module of navbox

import sys

output = 'work/navbox_output.txt'

def small_navbox():
    group_num = raw_input("How many groups would you like? Maximum of 20\n")

    if (group_num == str(1)):
        group_name1 = raw_input("What would you like the group name to be?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(2)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(3)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(4)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(5)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(6)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(7)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(8)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(9)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(10)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(11)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(12)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(13)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(14)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(15)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        group_name15 = raw_input("Fifteenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n|group15=" + group_name15 + "\n|list15=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(16)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        group_name15 = raw_input("Fifteenth?\n")
        group_name16 = raw_input("Sixteenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n|group15=" + group_name15 + "\n|list15=\n|group16=" + group_name16 + "\n|list16=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(17)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        group_name15 = raw_input("Fifteenth?\n")
        group_name16 = raw_input("Sixteenth?\n")
        group_name17 = raw_input("Seventeenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n|group15=" + group_name15 + "\n|list15=\n|group16=" + group_name16 + "\n|list16=\n|group17=" + group_name17 + "\n|list17=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(18)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        group_name15 = raw_input("Fifteenth?\n")
        group_name16 = raw_input("Sixteenth?\n")
        group_name17 = raw_input("Seventeenth?\n")
        group_name18 = raw_input("Eighteenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n|group15=" + group_name15 + "\n|list15=\n|group16=" + group_name16 + "\n|list16=\n|group17=" + group_name17 + "\n|list17=\n|group18=" + group_name18 + "\n|list18=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(19)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        group_name15 = raw_input("Fifteenth?\n")
        group_name16 = raw_input("Sixteenth?\n")
        group_name17 = raw_input("Seventeenth?\n")
        group_name18 = raw_input("Eighteenth?\n")
        group_name19 = raw_input("Nineteenth?\n")
        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n|group15=" + group_name15 + "\n|list15=\n|group16=" + group_name16 + "\n|list16=\n|group17=" + group_name17 + "\n|list17=\n|group18=" + group_name18 + "\n|list18=\n|group19=" + group_name19 + "\n|list19=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

    if (group_num == str(20)):
        group_name1 = raw_input("What would you like the first group name to be?\n")
        group_name2 = raw_input("What would you like the second group name to be?\n")
        group_name3 = raw_input("What would you like the third group name to be?\n")
        group_name4 = raw_input("What would you like the fourth group name to be?\n")
        group_name5 = raw_input("Fifth?\n")
        group_name6 = raw_input("Sixth?\n")
        group_name7 = raw_input("Seventh?\n")
        group_name8 = raw_input("Eighth?\n")
        group_name9 = raw_input("Ninth?\n")
        group_name10 = raw_input("Tenth?\n")
        group_name11 = raw_input("Eleventh?\n")
        group_name12 = raw_input("Twelfth?\n")
        group_name13 = raw_input("Thirteenth?\n")
        group_name14 = raw_input("Fourteenth?\n")
        group_name15 = raw_input("Fifteenth?\n")
        group_name16 = raw_input("Sixteenth?\n")
        group_name17 = raw_input("Seventeenth?\n")
        group_name18 = raw_input("Eighteenth?\n")
        group_name19 = raw_input("Nineteenth?\n")
        group_name20 = raw_input("Twentieth?\n")

        modname = raw_input("What mod is this for?\n")

        fileout = open(output, "w")
        fileout.write("{{Navbox\n|title={{L|" + modname + "}}\n|name=Navbox " + modname + "\n|titlestyle = background:#CCCCCC;\n|groupstyle = background:#DDDDDD;\n|group1=" + group_name1 + "\n|list1=\n|group2=" + group_name2 + "\n|list2=\n|group3=" + group_name3 + "\n|list3=\n|group4=" + group_name4 + "\n|list4=\n|group5=" + group_name5 + "\n|list5=\n|group6=" + group_name6 + "\n|list6=\n|group7=" + group_name7 + "\n|list7=\n|group8=" + group_name8 + "\n|list8=\n|group9=" + group_name9 + "\n|list9=\n|group10=" + group_name10 + "\n|list10=\n|group11=" + group_name11 + "\n|list11=\n|group12=" + group_name12 + "\n|list12=\n|group13=" + group_name13 + "\n|list13=\n|group14=" + group_name14 + "\n|list14=\n|group15=" + group_name15 + "\n|list15=\n|group16=" + group_name16 + "\n|list16=\n|group17=" + group_name17 + "\n|list17=\n|group18=" + group_name18 + "\n|list18=\n|group19=" + group_name19 + "\n|list19=\n|group20=" + group_name20 + "\n|list20=\n}}\n<noinclude>{{Navbox Applied Energistics/doc|the items in the [[" + modname + "]] mod}}</noinclude>")
        fileout.close()

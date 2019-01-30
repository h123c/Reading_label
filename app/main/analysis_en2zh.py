#encoding:utf-8

def class_analysis(DICT_data):
    DICT_analysis_template = {"A":{},"C": {},"D": {},"F": {},"I": {},"M": {},"N": {},"P": {},"R": {},"S": {},"T": {},"U": {},"V": {},"W": {},"Y": {},"others":{}}
    for en,zh in DICT_data.items():
        if en[0] in DICT_analysis_template.keys():
            DICT_analysis_template[en[0]][en] = zh#.decode("utf-8")
        else:DICT_analysis_template["others"][en] = zh#.decode("utf-8")
    return DICT_analysis_template


def get_sim(DICT_analysis_template,analysis_txt):
    res_sim = {}
    if analysis_txt[0] in DICT_analysis_template.keys():
        for k,v in DICT_analysis_template[analysis_txt[0]].items():
            en_list = k.split("#")
            zh_list = v.split("#")
            pre = analysis_txt[0]
            flag = 1

            for ind in xrange(len(en_list)):
                if en_list[ind] in [".",",","?","!"]:continue
                if ind%2 == 0:
                    #print en_list[ind],"\t",analysis_txt[analysis_txt.find(pre):]
                    if en_list[ind] not in analysis_txt[analysis_txt.find(pre):]:
                        flag = 0
                        #print en_list[ind],flag
                        break
            if flag == 0:continue
            else:res_sim[k] = v
        res = ["", ""]
        if len(res_sim.keys())>1:
            max_len = 0
            for ks,vs in res_sim.items():
                #print "备选:",ks
                ks_list = ks.split("#")
                l = 0
                for i in xrange(len(ks_list)):
                    if i%2 == 0:
                        l = l + len(ks_list[i])
                if l > max_len:
                    res[0] = ks
                    res[1] = vs
                    max_len = l
            return res[0],res[1]
        elif len(res_sim.keys()) == 1:
            for kss,vss in res_sim.items():
                return kss,vss
        return 1,0
    else:
        for k,v in DICT_analysis_template["others"].items():
            en_list = k.split("#")
            zh_list = v.split("#")
            pre = analysis_txt[0]
            flag = 1

            for ind in xrange(len(en_list)):
                if en_list[ind] in [".",",","?","!"]:continue
                if ind%2 == 0:
                    #print en_list[ind],"\t",analysis_txt[analysis_txt.find(pre):]
                    if en_list[ind] not in analysis_txt[analysis_txt.find(pre):]:
                        flag = 0
                        #print en_list[ind],flag
                        break
            if flag == 0:continue
            else:res_sim[k] = v
        res = ["", ""]
        if len(res_sim.keys())>1:
            max_len = 0
            for ks,vs in res_sim.items():
                ks_list = ks.split("#")
                l = 0
                for i in xrange(len(ks_list)):
                    if i%2 == 0:
                        l = l + len(ks_list[i])
                if l > max_len:
                    res[0] = ks
                    res[1] = vs
                    max_len = l
            return res[0],res[1]
        elif len(res_sim.keys()) == 1:
            for kss,vss in res_sim.items():
                return kss,vss
        return 1,0

def combine_analysis(en_txt,zh_txt,analysis):
    res = ""
    next_list = []
    pre_list = []
    if en_txt[0] == "#":types = 0
    else:types = 1
    en_list = en_txt.strip("#").split("#")
    #print "en_list:",en_list
    zh_list = zh_txt.split("#")
    #print "zh_list:", zh_list
    pre = analysis[0]
    for ind in xrange(len(en_list)):
        if ind % 2 == 0:
            #print analysis
            #print len(en_list[ind])-1
            pre_list.append(analysis[:len(en_list[ind])])
            analysis = analysis[len(en_list[ind])-1:]
            #print "sam1:",analysis
        else:
            #print "abc:",ind
            if ind < len(en_list)-1:
                #print "sam2:",en_list[ind+1]
                #print "analysis:",analysis
                next_ind = analysis.find(en_list[ind+1])
                #print "diff:",analysis[:next_ind]
                next_list.append(analysis[:next_ind])
                #print "1",analysis[:next_ind]
                analysis = analysis[next_ind:]
            else:
                #print "abc",ind,analysis
                next_list.append(analysis)
    #print "next_list:",next_list
    #print "pre_list:",pre_list
    for ind in xrange(len(en_list)):
        if types == 1:
            if ind % 2 == 1:
                res = res + next_list[(ind-1)/2]
            else:res = res + zh_list[ind]
        else:
            if ind % 2 == 1:
                res = res + pre_list[(ind-1)/2]
            else:res = res + zh_list[ind]
    return res


def en2zh_load():
    message_path = "/home/hc/Desktop/hexin/language/Web_demo/app/main/analysis_template/message_template.txt"
    rule_issue_path = "/home/hc/Desktop/hexin/language/Web_demo/app/main/analysis_template/rule_issueType.txt"
    shortMessage_path_ = "/home/hc/Desktop/hexin/language/Web_demo/app/main/analysis_template/shortMessage_.txt"

    def read_data(path):
        DICT_data = {}
        with open(path, "rb") as f:
            data = f.read().split("\n")
        for line in data:
            try:
                k, v = line.split("\t")
            except:
                continue
            DICT_data[k] = v.decode("utf-8")
        return DICT_data
    DICT_data = read_data(message_path)
    DICT_analysis_template = class_analysis(DICT_data)

    DICT_rule_issue = read_data(rule_issue_path)
    DICT_shortMessage = read_data(shortMessage_path_)
    return DICT_analysis_template,DICT_rule_issue,DICT_shortMessage

def en2zh_main(analysis_txt,DICT_analysis_template):
    #print "原句:",analysis_txt
    k, v = get_sim(DICT_analysis_template, analysis_txt)
    #print "匹配:", k, v
    if k == 1:
        return "\n"
    res = combine_analysis(k, v, analysis_txt)
    #print "结果:",res
    return res




if __name__ == "__main__":

    #单个测试
    path = "./analysis_template/message_template.txt"

    with open(path, "rb") as f:
        data = f.read().split("\n")
    DICT_data = {}
    for line in data:
        k, v = line.split("\t")
        DICT_data[k] = v
    DICT_analysis_template = class_analysis(DICT_data)

    analysis_txt = 'Please check whether an article is missing: "be a honest" or "be an honest"'
    #analysis_txt = "The pronoun 'We' must be used with a non-third-person form of a verb: 'mad'"
    #analysis_txt = 'If "Learning" is used as a verb, it usually requires the infinitive: "to paint".'
    #analysis_txt = 'The pronoun "she" is usually used with a third-person or a past tense verb: "schools", "schooled".'
    #analysis_txt = 'The words "come in" and "come to" have different meanings. "Come in my office" means "have an orgasm in my office." "Come to" or "Come into" means "enter." Did you mean "come to" or "come into"?'
    #analysis_txt = 'Possible agreement error. The noun good seems to be uncountable; consider using: "much good", "a good deal of good".'
    #analysis_txt = 'A determiner cannot combine with a possessive pronoun. Did you mean simply "my Good" or "the Good".'
    #analysis_txt = '"needs cut" is only accepted in certain dialects. For something more widely acceptable, try "cut" or "to be cut".'
    #analysis_txt = "Don't use indefinite articles with plural words. Did you mean 'eye'?"
    analysis_txt = 'Did you mean: "In the future"?'
    analysis_txt = 'Use only "taller" (without "More") when you use the comparative.'

    print "原句:",analysis_txt
    k, v = get_sim(DICT_analysis_template, analysis_txt)
    print "匹配:",k,v
    res = combine_analysis(k, v, analysis_txt)
    print "结果:",res


    #综合测试
    new_path = "./translate_data/message_.txt"
    with open(new_path, "rb") as f:
        data = f.read().split("\n")

    DICT_analysis_template,DICT_rule_issue,DICT_shortMessage = en2zh_load()
    for line in data[9001:]:
        en2zh_main(line, DICT_analysis_template)
    #print res



"""
Commas set off the month in a weekday-month-day date: #"Sunday,"#.	逗号在工作日、月日、星期日、#"Sunday,"#中抵消了月份。  ****
Did you mean #"calendar"#, a system of organizing days? A 'calender' is a machine.	你的意思是#"calendar"#，一个组织日子的系统吗？“日历”是一台机器。  ***
Did you mean #"will ,"# or is a hyphen missing #"ill-,"# (e.g., #ill-treated, ill-advised#)?	你的意思是#"will ,"#，or is a hyphen missing，#“ill-，”#（例如，#虐待，不明智#）？  ****
Maybe you need to remove one determiner so that only #"A"# or #"A"# is left.	也许你需要去掉一个洗涤剂，这样就只剩下#"A"#或#"A"#。 ***
One of these determiners is redundant in this context. Choose only one: #"a room" or "another room"#.	在这种情况下，其中一个威慑者是多余的。只选择一个：#"a room" or "another room"#。  ***
When referring to yourself and somebody else, put their name first. Also check whether the nominative form "I" is required here.	当提到你自己和别人时，把他们的名字放在第一位。还要检查这里是否需要提名表格“I”。  ***
Writing for an international audience? Consider adding the metric equivalent.	为国际观众写作？考虑添加公制等效值。  ***
"""
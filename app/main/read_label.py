# #encoding:utf-8
path3 = "./app/label_data/label3.txt"
path2 = "./app/label_data/label2.txt"
path1 = "./app/label_data/label1.txt"

#path3 = "/home/hc/Desktop/hexin/manual_tag/Web_label/app/label_data/label3.txt"
#path2 = "/home/hc/Desktop/hexin/manual_tag/Web_label/app/label_data/label2.txt"
#path1 = "/home/hc/Desktop/hexin/manual_tag/Web_label/app/label_data/label1.txt"
def get_label(path):
    id_list = []
    name_list = []
    with open(path,"rb") as f:
        data_list = f.read().decode("utf-8").split("\n")
    for line in data_list:
        if " " in line:
            name,id = line.split(" ")
            id_list.append(id)
            name_list.append(name)
    return name_list,id_list

label_data = {}
name_list1, id_list1 = get_label(path1)
name_list2, id_list2 = get_label(path2)
name_list3, id_list3 = get_label(path3)

three_id2name = {}
for i in range(len(name_list3)):
    three_id2name[id_list3[i]] = name_list3[i]

two_id2name = {}
for i in range(len(name_list2)):
    two_id2name[id_list2[i]] = name_list2[i]

two2one = {u'586': u'586', u'587': u'586', u'601': u'586', u'610': u'610', u'611': u'610', u'641': u'610', u'614': u'610', u'630': u'610', u'647': u'646', u'646': u'646', u'649': u'646', u'659': u'646', u'656': u'646'}
three2one = {u'591': u'586', u'590': u'586', u'593': u'586', u'592': u'586', u'595': u'586', u'594': u'586', u'597': u'586', u'596': u'586', u'599': u'586', u'598': u'586', u'629': u'610', u'628': u'610', u'609': u'586', u'607': u'586', u'631': u'610', u'660': u'646', u'625': u'610', u'606': u'586', u'605': u'586', u'601': u'601', u'621': u'610', u'600': u'586', u'604': u'586', u'641': u'641', u'603': u'586', u'657': u'646', u'602': u'586', u'632': u'610', u'633': u'610', u'624': u'610', u'638': u'610', u'654': u'646', u'655': u'646', u'608': u'586', u'653': u'646', u'650': u'646', u'639': u'610', u'620': u'610', u'645': u'610', u'658': u'646', u'659': u'659', u'586': u'586', u'587': u'587', u'618': u'610', u'619': u'610', u'634': u'610', u'635': u'610', u'636': u'610', u'637': u'610', u'612': u'610', u'613': u'610', u'610': u'610', u'611': u'611', u'616': u'610', u'617': u'610', u'588': u'586', u'589': u'586', u'651': u'646', u'614': u'614', u'627': u'610', u'615': u'610', u'623': u'610', u'652': u'646', u'661': u'646', u'630': u'630', u'640': u'610', u'643': u'610', u'642': u'610', u'626': u'610', u'644': u'610', u'647': u'647', u'646': u'646', u'649': u'649', u'648': u'646', u'622': u'610', u'656': u'656'}
three2two = {u'591': u'587', u'590': u'587', u'593': u'587', u'592': u'587', u'595': u'587', u'594': u'587', u'597': u'587', u'596': u'587', u'599': u'587', u'598': u'587', u'629': u'614', u'628': u'614', u'609': u'601', u'607': u'601', u'631': u'630', u'660': u'659', u'625': u'614', u'606': u'601', u'605': u'601', u'601': u'601', u'621': u'614', u'600': u'587', u'604': u'601', u'656': u'656', u'603': u'601', u'657': u'656', u'602': u'601', u'632': u'630', u'624': u'614', u'638': u'630', u'654': u'649', u'655': u'649', u'608': u'601', u'653': u'649', u'650': u'649', u'639': u'630', u'620': u'614', u'645': u'641', u'658': u'656', u'659': u'659', u'630': u'630', u'587': u'587', u'618': u'614', u'619': u'614', u'634': u'630', u'635': u'630', u'636': u'630', u'637': u'630', u'612': u'611', u'613': u'611', u'633': u'630', u'611': u'611', u'616': u'614', u'617': u'614', u'588': u'587', u'589': u'587', u'651': u'649', u'614': u'614', u'627': u'614', u'615': u'614', u'623': u'614', u'661': u'659', u'641': u'641', u'640': u'630', u'643': u'641', u'642': u'641', u'626': u'614', u'644': u'641', u'647': u'647', u'652': u'649', u'649': u'649', u'648': u'647', u'622': u'614'}
two_include = {u'630': [u'640', u'631', u'632', u'634', u'636', u'637', u'638', u'639', u'633', u'635'], u'587': [u'590', u'593', u'592', u'595', u'594', u'597', u'596', u'599', u'598', u'589', u'600', u'588', u'591'], u'601': [u'607', u'606', u'605', u'609', u'604', u'602', u'603', u'608'], u'611': [u'613', u'612'], u'641': [u'643', u'642', u'645', u'644'], u'614': [u'628', u'621', u'625', u'626', u'620', u'619', u'616', u'617', u'618', u'629', u'627', u'624', u'623', u'615', u'622'], u'656': [u'657', u'658'], u'647': [u'648'], u'649': [u'655', u'652', u'653', u'650', u'651', u'654'], u'659': [u'660', u'661']}
label_data = {"two_id2name":two_id2name,"three_id2name":three_id2name,"name_list1":name_list1,"name_list2":name_list2,"name_list3":name_list3,"id_list1":id_list1,"id_list2":id_list2,"id_list3":id_list3,"two2one":two2one,"three2one":three2one,"three2two":three2two,"two_include":two_include}

if __name__ == "__main__":

    name_list3, id_list3 = get_label(path3)
    print(name_list3)
    print(id_list3)
    three_id2name = {}
    for i in xrange(len(name_list3)):
        three_id2name[id_list3[i]] = name_list3[i]
    print(three_id2name)
    for k,v in three_id2name.items():
        print(k,v)

    print(label_data["two_include"]["611"][0])
    #label_data["three_id2name"][label_data["two_include"][id][line]]

# three2two = {u'591': u'587', u'590': u'587', u'593': u'587', u'592': u'587', u'595': u'587', u'594': u'587', u'597': u'587', u'596': u'587', u'599': u'587', u'598': u'587', u'629': u'614', u'628': u'614', u'609': u'601', u'607': u'601', u'631': u'630', u'660': u'659', u'625': u'614', u'606': u'601', u'605': u'601', u'601': u'601', u'621': u'614', u'600': u'587', u'604': u'601', u'656': u'656', u'603': u'601', u'657': u'656', u'602': u'601', u'632': u'630', u'624': u'614', u'638': u'630', u'654': u'649', u'655': u'649', u'608': u'601', u'653': u'649', u'650': u'649', u'639': u'630', u'620': u'614', u'645': u'641', u'658': u'656', u'659': u'659', u'630': u'630', u'587': u'587', u'618': u'614', u'619': u'614', u'634': u'630', u'635': u'630', u'636': u'630', u'637': u'630', u'612': u'611', u'613': u'611', u'633': u'630', u'611': u'611', u'616': u'614', u'617': u'614', u'588': u'587', u'589': u'587', u'651': u'649', u'614': u'614', u'627': u'614', u'615': u'614', u'623': u'614', u'661': u'659', u'641': u'641', u'640': u'630', u'643': u'641', u'642': u'641', u'626': u'614', u'644': u'641', u'647': u'647', u'652': u'649', u'649': u'649', u'648': u'647', u'622': u'614'}
#
# two = set(three2two.values())
# three = three2two.keys()
#
# two = [u'630', u'587', u'601', u'611', u'641', u'614', u'656', u'647', u'649', u'659']
# two_include = {}
# for k,v in three2two.items():
#     if v in two_include.keys():
#         two_include[v].append(k)
#     else:
#         two_include[v] = []
# print two_include

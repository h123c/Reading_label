#encoding:utf-8
from flask import Blueprint, request, render_template
from app.main.read_label import label_data
import os
import shutil

user_blueprint = Blueprint('home', __name__)

path = "./data/"
outpath = "./output/"
def get_file_list(path):
    file_list = os.listdir(path)
    return file_list

def read_file(file_path):
    with open(file_path,"rb") as f:
        data = f.read().decode("utf-8")
    return data
def write_file(file_name,data):
    with open(outpath+file_name,"wb") as f:
        f.write(data.encode("utf-8"))


@user_blueprint.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        global file_list
        file_list = get_file_list(path)
        if len(file_list) == 0:
            return render_template('index.html', txt="", file=u"no file", file_num=0, label_data=label_data)
        txt = read_file(os.path.join(path,file_list[0]))
        file_num = len(file_list)
        return render_template('index.html',txt = txt,file=file_list[0],file_num=file_num,label_data = label_data)

@user_blueprint.route('/change', methods=['GET','POST'])
def get_change():
    if request.method == 'GET':
        type = request.args.get("type")
        file = request.args.get("file")
        if file == u"no file":
            return render_template('index.html', txt="", file=file, file_num=0, label_data=label_data)

        file_list = get_file_list(path)
        try:
            ind = file_list.index(file)
        except:
            file_list = get_file_list(path)
            ind = file_list.index(file)
        file_num = len(file_list)
        if type == "next":
            if ind < file_num-1:
                new_file = file_list[ind+1]
            else:
                new_file = file_list[ind]
        elif type == "pre":
            if ind ==0:
                new_file = file_list[ind]
            else:
                new_file = file_list[ind-1]
        txt = read_file(os.path.join(path, new_file))

        return render_template('index.html',txt = txt,file =new_file,file_num=file_num,label_data=label_data)

@user_blueprint.route('/label', methods=['GET','POST'])
def get_label():
    if request.method == 'GET':
        id = request.args.get("id")
        file = request.args.get("file")
        if file == u"no file":
            return render_template('index.html', txt="", file=file, file_num=0, label_data=label_data)

        txt = read_file(os.path.join(path, file))
        if "__label__" not in txt:
            new = txt+u"__label__"+id
        else:
            new = txt[:txt.find(u"__label__")] + u"__label__" + id
        write_file(file, new)
        if os.path.getsize(os.path.join(outpath, file)) >= os.path.getsize(os.path.join(path, file)):
            os.remove(path+file)
        try:
            file_list.remove(file)
        except:
            file_list = get_file_list(path)
        file_num = len(file_list)
        if file_num == 0:
            txt = ""
            new_file = u"no file"
        else:
            txt = read_file(os.path.join(path, file_list[0]))
            new_file = file_list[0]
        return render_template('index.html',txt = txt,file =new_file,file_num=file_num,label_data=label_data)

@user_blueprint.route('/count', methods=['GET','POST'])
def get_count():
    if request.method == 'GET':
        file_list = get_file_list(outpath)
        count_res = {}
        undeal = {"num":0,"name":[]}
        for file in file_list:
            with open(os.path.join(outpath, file),"rb") as f:
                txt = f.read().decode("utf-8")
            if u"__label__" not in txt:
                undeal["num"] +=1
                undeal["name"].append(file)
                continue
            label = txt[txt.find(u"__label__")+9:]
            count_res[label_data["three2two"][label]] = count_res.get(label_data["three2two"][label],0) + 1
        total = sum(count_res.values())

        return render_template('dealed.html',count_res = count_res,total=total, label_data=label_data,undeal=undeal)

@user_blueprint.route('/relabel', methods=['GET','POST'])
def get_relabel():
    if request.method == 'GET':
        global file_list
        file_list = get_file_list(outpath)
        for file in file_list:
            with open(os.path.join(outpath, file),"rb") as f:
                txt = f.read().decode("utf-8")
            if u"__label__" not in txt:
                shutil.move(outpath+file, path+file)
            else:
                continue

        file_list = get_file_list(path)

        if len(file_list) == 0:
            return render_template('index.html', txt="", file=u"no file", file_num=0, label_data=label_data)
        txt = read_file(os.path.join(path, file_list[0]))
        file_num = len(file_list)
        return render_template('index.html', txt=txt, file=file_list[0], file_num=file_num, label_data=label_data)



error_blueprint = Blueprint('error', __name__)
@error_blueprint.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html')


"""
3
话题 - 人与自我 586
	生活与学习 587
		个人 588
		认识自我 594
		社区 590
		学校生活 591
		健康的生活方式 592
		家庭 589
		积极的生活态度 593
		丰富自我 595
		完善自我 596
		乐于学习 597
		善于学习 598
		终身学习 599
		语言学习规律、方法 600
	做人与做事 601
		优秀品行 602
		正确的人生态度 603
		公民义务与社会责任 604
		生活的意义与价值 605
		未来职业发展趋势 606
		个人职业倾向 607
		个人未来规划 608
		创新与创业意识 609
话题 - 人与社会 610
	社会服务与人际沟通 611
		良好的人际关系与社会交往 612
		公益事业与志愿服务 613
	文学、艺术与体育 614
		文学名著 621
		绘画领域代表性作品和人物 622
		诗歌 617
		传记 618
		文学简史 619
		戏剧 616
		经典演讲 620
		小说 615
		建筑领域代表性作品和人物 623
		影视领域的概况及其发展 624
		音乐领域的概况及其发展 625
		体育活动 626
		大型体育赛事 627
		体育与健康 628
		体育精神 629
	历史、社会与文化 630
		不同民族文化习俗与传统节日 631
		对社会有突出贡献的人物 632
		重要国际组织与社会公益机构 633
		法律常识与法治意识 634
		物质与非物质文化遗产 635
		社会热点问题 636
		重大政治 637
		历史事件 638
		文化渊源 639
		社会进步与人类文明 640
	科学与技术 641
		科技发展 642
		信息技术创新 643
		科学精神 644
		信息安全 645
话题 - 人与自然 646
	自然生态 647
		主要国家地理概况 648
	环境保护 649
		自然环境 650
		自然遗产保护 651
		人与环境 652
		人与动植物 653
		人类生存 654
		社会发展与环境的关系 655
	灾害防范 656
		自然灾害与防范 657
		安全常识与自我保护 658
	宇宙探索 659
		自然科学研究成果 660
		地球与宇宙奥秘探索 661
		
		
two2one = {'586': '586', '587': '586', '601': '586', '610': '610', '611': '610', '641': '610', '614': '610', '630': '610', '647': '646', '646': '646', '649': '646', '659': '646', '656': '646'}
three2one = {'591': '586', '590': '586', '593': '586', '592': '586', '595': '586', '594': '586', '597': '586', '596': '586', '599': '586', '598': '586', '629': '610', '628': '610', '609': '586', '607': '586', '631': '610', '660': '646', '625': '610', '606': '586', '605': '586', '601': '601', '621': '610', '600': '586', '604': '586', '641': '641', '603': '586', '657': '646', '602': '586', '632': '610', '633': '610', '624': '610', '638': '610', '654': '646', '655': '646', '608': '586', '653': '646', '650': '646', '639': '610', '620': '610', '645': '610', '658': '646', '659': '659', '586': '586', '587': '587', '618': '610', '619': '610', '634': '610', '635': '610', '636': '610', '637': '610', '612': '610', '613': '610', '610': '610', '611': '611', '616': '610', '617': '610', '588': '586', '589': '586', '651': '646', '614': '614', '627': '610', '615': '610', '623': '610', '652': '646', '661': '646', '630': '630', '640': '610', '643': '610', '642': '610', '626': '610', '644': '610', '647': '647', '646': '646', '649': '649', '648': '646', '622': '610', '656': '656'}
three2two = {'591': '587', '590': '587', '593': '587', '592': '587', '595': '587', '594': '587', '597': '587', '596': '587', '599': '587', '598': '587', '629': '614', '628': '614', '609': '601', '607': '601', '631': '630', '660': '659', '625': '614', '606': '601', '605': '601', '601': '601', '621': '614', '600': '587', '604': '601', '656': '656', '603': '601', '657': '656', '602': '601', '632': '630', '624': '614', '638': '630', '654': '649', '655': '649', '608': '601', '653': '649', '650': '649', '639': '630', '620': '614', '645': '641', '658': '656', '659': '659', '630': '630', '587': '587', '618': '614', '619': '614', '634': '630', '635': '630', '636': '630', '637': '630', '612': '611', '613': '611', '633': '630', '611': '611', '616': '614', '617': '614', '588': '587', '589': '587', '651': '649', '614': '614', '627': '614', '615': '614', '623': '614', '661': '659', '641': '641', '640': '630', '643': '641', '642': '641', '626': '614', '644': '641', '647': '647', '652': '649', '649': '649', '648': '647', '622': '614'}

three_name = [u"个人",u"认识自我",u"社区",u"学校生活",u"健康的生活方式",u"家庭",u"积极的生活态度",u"丰富自我",u"完善自我",u"乐于学习",u"善于学习",u"终身学习",u"语言学习规律、方法",u"优秀品行",u"正确的人生态度",u"公民义务与社会责任",u"生活的意义与价值",\
u"未来职业发展趋势",u"个人职业倾向",u"个人未来规划",u"创新与创业意识",u"良好的人际关系与社会交往",u"公益事业与志愿服务",u"文学名著",u"",u"",u"",u"",u"",u""]
  three_id = [u"588",u"594",u"590",u"591",u"592",u"589",u"593",u"595",u"596",u"597",u"598",u"599",u"600",u"602",u"603",u"604",u"605",\
  u"606",u"607",u"608",u"609",u"612",u"613",u"621",u"",u"",u"",u"",u"",u"",u""]

		
		
		<li>
					<form action="get_essay" method="post" id="width100">
                            <textarea style="height:800px;" id ="inp_text"  type="text" name="essay" required>{% if body %}{{ body }}{% else %}{% endif %}</textarea><br>
							<label><input name="lab" type="radio" value="0" checked/>一级 </label>
							<label><input name="lab" type="radio" value="1" />二级 </label>
							<label><input name="lab" type="radio" value="2" />三级 </label>
  						<input id ="inp_sub" class ="b_right" type="submit" value="开始分析"/>
					</form>
				</li>
				
<tr><td>生活与学习</td>     <td>做人与做事</td>		<td>社会服务与人际沟通</td>      <td>文学、艺术与体育</td>         <td>历史、社会与文化</td>             <td>科学与技术</td>    <td>自然生态</td>         <td>环境保护</td>           <td>灾害防范</td><td>宇宙探索</td></tr>				
<tr><td>个人</td>          <td>优秀品行</td>			<td>良好的人际关系与社会交往</td><td>文学名著</td>                <td>不同民族文化习俗与传统节日</td>     <td>科技发展</td>      <td>主要国家地理概况</td>  <td>自然环境</td>            <td>自然灾害与防范</td><td>宇宙探索</td></tr>
					<tr><td>认识自我</td>       <td>正确的人生态度</td>		<td>公益事业与志愿服务</td>      <td>绘画领域代表性作品和人物</td>  <td>对社会有突出贡献的人物</td>        <td>信息技术创新</td>  <td>               </td>  <td>自然遗产保护</td>       <td>安全常识与自我保护</td><td>宇宙探索</td></tr>
					<tr><td>社区</td>          <td>公民义务与社会责任</td>	<td>					</td><td>诗歌</td>                    <td>重要国际组织与社会公益机构</td>     <td>科学精神</td>        <td>            </td>   <td>人与环境</td>          <td>                 </td><td>宇宙探索</td></tr>
					<tr><td>学校生活</td>      <td>生活的意义与价值</td>	<td>					</td><td>传记</td>                    <td>法律常识与法治意识</td>             <td>信息安全</td>       <td>             </td>  <td>人与动植物</td>        <td>                   </td><td>宇宙探索</td></tr>
					<tr><td>健康的生活方式</td> <td>未来职业发展趋势</td>	<td>					</td><td>文学简史</td>                  <td>物质与非物质文化遗产</td>         <td>        </td>       <td>            </td>   <td>人类生存</td>         <td>                  </td><td>宇宙探索</td></tr>
					<tr><td>家庭</td>          <td>个人职业倾向</td>		<td>					</td><td>戏剧</td>                    <td>社会热点问题</td>                 <td>        </td>       <td>             </td>  <td>社会发展与环境的关系</td><td>                 </td><td>宇宙探索</td></tr>
					<tr><td>积极的生活态度</td>  <td>个人未来规划</td>		<td>					</td><td>经典演讲</td>                  <td>重大政治</td>                  <td>         </td>       <td>            </td>   <td>                </td><td>                   </td><td>宇宙探索</td></tr>
					<tr><td>丰富自我</td>       <td>创新与创业意识</td>		<td>					</td><td>小说</td>                    <td>历史事件</td>                   <td>            </td>     <td>              </td> <td>                </td><td>                     </td><td>宇宙探索</td></tr>
					<tr><td>完善自我</td>       <td>         </td>		<td>					</td><td>建筑领域代表性作品和人物</td>    <td>文化渊源</td>                   <td>          </td>     <td>              </td>  <td>                 </td><td>                   </td><td>宇宙探索</td></tr>
					<tr><td>乐于学习</td>       <td>    		</td>		<td>					</td><td>影视领域的概况及其发展</td>      <td>社会进步与人类文明</td>           <td>            </td>   <td>            </td>   <td>                 </td><td>                      </td><td>宇宙探索</td></tr>
					<tr><td>善于学习</td>       <td>			</td>		<td>					</td><td>音乐领域的概况及其发展</td>      <td>                  </td>         <td>         </td>      <td>             </td>  <td>                 </td><td>                   </td><td>宇宙探索</td></tr>
					<tr><td>终身学习</td>       <td>			</td>		<td>					</td><td>体育活动</td>                  <td>                  </td>         <td>           </td>    <td>            </td>   <td>                </td><td>                   </td><td>宇宙探索</td></tr>
					<tr><td>        </td>       <td>		</td>		<td>					</td><td>大型体育赛事</td>               <td>                  </td>         <td>         </td>      <td>             </td>  <td>                 </td><td>                   </td><td>宇宙探索</td></tr>
					<tr><td>        </td>       <td>		</td>		<td>					</td><td>体育与健康</td>                 <td>                 </td>         <td>         </td>       <td>            </td>   <td>                 </td><td>                  </td><td>宇宙探索</td></tr>
					<tr><td>        </td>       <td>		</td>		<td>					</td><td>体育精神</td>                  <td>                  </td>         <td>        </td>       <td>            </td>   <td>                  </td><td>                 </td><td>宇宙探索</td></tr>

<a href="label?file={{ file }}&id={{ label_data['two_include'][id][line] }}">
"""
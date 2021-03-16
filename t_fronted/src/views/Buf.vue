<!--
 * @Author: your name
 * @Date: 2021-03-08 11:01:21
 * @LastEditTime: 2021-03-16 21:36:24
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /t_fronted/src/Buf.vue
-->


<template>
  <div>
    <el-header style="text-align: center; font-size: 40px">
    <span>教师管理系统</span>
    </el-header>
    <el-table
    :data="tableData.filter(data => !search || data.teacher_name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%"
    height="400">
    <el-table-column type="expand">
      <template #default="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="name">
            <span>{{ props.row.teacher_name }}</span>
          </el-form-item>
          <el-form-item label="age">
            <span>{{ props.row.teacher_age }}</span>
          </el-form-item>
          <el-form-item label="sex">
            <span>{{ props.row.teacher_sex }}</span>
          </el-form-item>
          <el-form-item label="major">
            <span>{{ props.row.teacher_major }}</span>
          </el-form-item>
          <el-form-item label="department">
            <span>{{ props.row.teacher_department }}</span>
          </el-form-item>
          <el-form-item label="college">
            <span>{{ props.row.teacher_college }}</span>
          </el-form-item>
          <el-form-item label="address">
            <span>{{ props.row.teacher_address }}</span>
          </el-form-item>
          <el-form-item label="phone">
            <span>{{ props.row.teacher_phone }}</span>
          </el-form-item>
          <el-form-item label="salary">
            <span>{{ props.row.teacher_salary }}</span>
          </el-form-item>
          <el-form-item label="degree">
            <span>{{ props.row.teacher_degree }}</span>
          </el-form-item>
          <el-form-item label="hobby">
            <span>{{ props.row.teacher_hobby }}</span>
          </el-form-item>
          <el-form-item label="height">
            <span>{{ props.row.teacher_heigth }}</span>
          </el-form-item>
          <el-form-item label="weight">
            <span>{{ props.row.teacher_weight }}</span>
          </el-form-item>
          <el-form-item label="married">
            <span>{{ props.row.teacher_ismarry}}</span>
             </el-form-item>
          </el-form>
      </template>
    </el-table-column>

    <el-table-column
      label="Name"
      prop="teacher_name"
      width="100">
    </el-table-column>
    <el-table-column
      label="Age"
      prop="teacher_age"
      width="100">
    </el-table-column>
    <el-table-column
      label="Sex"
      prop="teacher_sex"
      width="100">
    </el-table-column>
    <el-table-column
      label="Major"
      prop="teacher_major">
    </el-table-column>
    <el-table-column
      label="Department"
      prop="teacher_department">
    </el-table-column>
    
    <el-table-column
      align="right">
      <template #header>
        <el-input
          v-model="search"
          size="mini"
          placeholder="输入关键字搜索"/>
      </template>
      
      <template #default="scope">
        <el-button
          size="mini"
          type="primary"
          icon="el-icon-edit" circle
          @click="handleEdit(scope.$index, scope.row)"></el-button>

        <el-dialog title="个人信息" :visible.sync="dialogFormVisible" center="true">
  
          <el-form :model="form" :inline="true" :rules="rules" size="mini">

            <el-form-item prop="name" label="name" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            
            <el-form-item prop="age" label="age" :label-width="formLabelWidth">
              <el-input-number v-model="form.age" :min="1" :max="100" label="年龄"></el-input-number>
             </el-form-item>

            <el-form-item prop="sex" label="sex" :label-width="formLabelWidth">
              <el-select v-model="form.sex" placeholder="请选择">
                <el-option
                  v-for="item in sex"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
             </el-form-item>

            <el-form-item prop="major" label="major" :label-width="formLabelWidth">
              <el-input v-model="form.major" autocomplete="off">
              </el-input>
               </el-form-item>

            <el-form-item prop="department" label="department" :label-width="formLabelWidth">
              <el-input v-model="form.department" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="college" label="college" :label-width="formLabelWidth">
              <el-input v-model="form.college" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="address" label="address" :label-width="formLabelWidth">
              <el-input v-model="form.address" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="phone" label="phone" :label-width="formLabelWidth">
              <el-input v-model="form.phone" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="salary" label="salary" :label-width="formLabelWidth">
              <el-input v-model="form.salary" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="degree" label="degree" :label-width="formLabelWidth">
              <el-input v-model="form.degree" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="hobby" label="hobby" :label-width="formLabelWidth">
              <el-input v-model="form.hobby" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="height" label="height" :label-width="formLabelWidth">
              <el-input v-model="form.height" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="weight" label="weight" :label-width="formLabelWidth">
              <el-input v-model="form.weight" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="married" label="married" :label-width="formLabelWidth">
              <el-input v-model="form.marry" autocomplete="off">
              </el-input>
             </el-form-item>
          </el-form>

          <template #footer>
            <span class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="primary" @click="handleEdit2">确 定</el-button>
            </span>
          </template>
  
        </el-dialog>  

        <el-button
          size="mini"
          type="danger"
          icon="el-icon-delete" circle
          @click="handleDelete(scope.$index, scope.row)"></el-button> 
      </template>
    </el-table-column>
  </el-table>

  <div class="foot">
  <div>
    <el-pagination
      small
      layout="prev, pager, next"
      :page-size="num"
      :total="total_elements"
      @current-change="page">
    </el-pagination>
    </div>

  <div>
  <el-button type="text" @click="handleCreate">添加数据</el-button>
  <el-dialog title="添加新信息" :visible.sync="createdialogFormVisible" center="true">
  
          <el-form :model="form" :rules="rules" :inline="true" size="mini">

            <el-form-item prop="name" label="name" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off" size="small"></el-input>
            </el-form-item>
            
            <el-form-item prop="age" label="age" :label-width="formLabelWidth">
              <el-input-number v-model="form.age" :min="1" :max="100" label="年龄"></el-input-number>
             </el-form-item>

            <el-form-item prop="sex" label="sex" :label-width="formLabelWidth">
              <el-select v-model="form.sex" placeholder="请选择">
                <el-option
                  v-for="item in sex"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
             </el-form-item>

            <el-form-item prop="major" label="major" :label-width="formLabelWidth">
              <el-input v-model="form.major" autocomplete="off">
              </el-input>
               </el-form-item>

            <el-form-item prop="department" label="department" :label-width="formLabelWidth">
              <el-input v-model="form.department" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="college" label="college" :label-width="formLabelWidth">
              <el-input v-model="form.college" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="address" label="address" :label-width="formLabelWidth">
              <el-input v-model="form.address" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="phone" label="phone" :label-width="formLabelWidth">
              <el-input v-model="form.phone" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="salary" label="salary" :label-width="formLabelWidth">
              <el-input v-model="form.salary" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="degree" label="degree" :label-width="formLabelWidth">
              <el-input v-model="form.degree" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="hobby" label="hobby" :label-width="formLabelWidth">
              <el-input v-model="form.hobby" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="height" label="height" :label-width="formLabelWidth">
              <el-input v-model="form.height" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="weight" label="weight" :label-width="formLabelWidth">
              <el-input v-model="form.weight" autocomplete="off">
              </el-input>
             </el-form-item>
             <el-form-item prop="married" label="married" :label-width="formLabelWidth">
              <el-input v-model="form.marry" autocomplete="off">
              </el-input>
             </el-form-item>

          </el-form>

          <template #footer>
            <span class="dialog-footer">
              <el-button @click="createdialogFormVisible=false">取 消</el-button>
              <el-button type="primary" @click="Create">确 定</el-button>
            </span>
          </template>
  
        </el-dialog>
  </div>
  </div>

  </div>
</template>


<script>
  export default {
    data(){
      return {
        tableData:null,
        search: '',
        total_elements:null,
        dialogFormVisible: false,
        createdialogFormVisible:false,
        formLabelWidth:'120px',
        cur_row:null,
        num:6,
        sex:[
          {
          value: "男",
          label: '男'
        }, {
          value: '女',
          label: '女'
        },
        ],
        form:{
          id:"-1",
          name:"",
          sex:"",
          age:"",
          major:"",
          department:"",
          college:"",
          address:"",
          salary:"",
          phone:"",
          hobby:"",
          weight:"",
          height:"",
          marry:"",
          degree:""
        },
        rules: {
          name: [
            { required: true, message: '请输入姓名', trigger: 'blur' },
            { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
          ],
          age: [
            { required: true, message: '请填写年龄', trigger: 'change' }
          ],
          sex: [
            {required: true, message: '请填写性别', trigger: 'change' }
          ],
          major: [
            {required: true, message: '请填写专业', trigger: 'change' }
          ],
          department: [
            {required: true, message: '请填写教师学院', trigger: 'change' }
          ],
          resource: [
            { required: true, message: '请选择活动资源', trigger: 'change' }
          ],
          desc: [
            { required: true, message: '请填写活动形式', trigger: 'blur' }
          ]
        }
      }
    },

    methods: {

      clearbuf(){
        this.id="-1";
        this.form.name="";
        this.form.age="";
        this.form.sex="";
        this.form.major="";
        this.form.department="";
      },
      
      page(currentPage){
        var api="http://localhost:8000/api/list?page="+currentPage+"&num="+this.num;
        axios.get(api)
        .then(res => {
          this.tableData=res.data.data;
        })
        .catch(err => {
          console.error(err); 
        });
      },

      handleCreate(){
        this.createdialogFormVisible=true;
        this.new=true;
        this.clearbuf();
        // console.log(this.new);
        // console.log(this.createdialogFormVisible);
      },
      // cancelCreate(){
      //   this.createdialogFormVisible=false;
      // },
      Create(){
        this.createdialogFormVisible=false;
        console.log(this.createdialogFormVisible)
        var api="http://localhost:8000/api/create";
        axios.post(api,{
            name:this.form.name,
            major:this.form.major,
            sex:this.form.sex,
            age:this.form.age,
            department:this.form.department,
        })
        .then(res=>{
          this.total_elements=this.total_elements+1;
          window.location.reload();
          // console.log(this.tableData);
        })
        .catch(error=>{
          console.log(error)
        })
      ;
      },
      
      handleEdit(index, row){
        this.cur_row=index;
        this.dialogFormVisible=true;
        this.form.id=row.id
        this.form.name=row.teacher_name;
        this.form.age=row.teacher_age;
        this.form.sex=row.teacher_sex;
        this.form.major=row.teacher_major;
        this.form.department=row.teacher_department;

        console.log(index,row);
      },
      handleEdit2(){
        this.dialogFormVisible=false;
        console.log(this.form);
        // console.log(this.cur_row);
        var api="http://localhost:8000/api/update";
        
        axios.post(api,{
            id:this.form.id,
            name:this.form.name,
            major:this.form.major,
            sex:this.form.sex,
            age:this.form.age,
            department:this.form.department,
        })
        .then(res=>{
          console.log(res);
          this.tableData[this.cur_row].teacher_name=this.form.name;
          this.tableData[this.cur_row].teacher_age=this.form.age;
          this.tableData[this.cur_row].teacher_sex=this.form.sex;
          this.tableData[this.cur_row].teacher_major=this.form.major;
          this.tableData[this.cur_row].teacher_department=this.form.department;
          // console.log(this.tableData);
        });
      },
      
      handleDelete(index, row) {
        // console.log(index, row);
        const _this=this;
        var api="http://localhost:8000/api/delete?id="+row.id;

        this.$confirm("是否确定删除"+row.teacher_name,"提示",{
          confirmButtonText:"确定",
          cancelButtonText:"取消",
          type:"warning"
        }).then(()=> {
          axios.delete(api)
          .then(()=>{
            window.location.reload()
          })
          .catch(function(error){
            console.log(error)
          })
        })
      },
    },
    
    created(){
      var api="http://localhost:8000/api/list?page=1&num="+this.num;
      axios.get(api)
      .then(res => {
        console.log(res.data)
        this.tableData=res.data.data;
        this.total_elements=res.data.total
      })
      .catch(err => {
        console.error(err); 
      });
    },
    }

    
</script>

<style>
.foot{
  display:-webkit-flex;
  justify-content: space-between;

}

.demo-table-expand {
    font-size: 0;
  }
  
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}

.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 30%;
  }

.el-header {
    color: #333;
    line-height: 60px;
  }
</style>

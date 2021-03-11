<!--
 * @Author: your name
 * @Date: 2021-03-08 11:01:21
 * @LastEditTime: 2021-03-10 23:01:49
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /t_fronted/src/Buf.vue
-->


<template>
  <div>
    <el-table
    :data="tableData.filter(data => !search || data.teacher_name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%">
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
  
          <el-form :model="form">

            <el-form-item label="name" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            
            <el-form-item label="age" :label-width="formLabelWidth">
              <el-input v-model="form.age" autocomplete="off">
              </el-input>
             </el-form-item>

            <el-form-item label="sex" :label-width="formLabelWidth">
              <el-input v-model="form.sex" autocomplete="off">
              </el-input>
             </el-form-item>

            <el-form-item label="major" :label-width="formLabelWidth">
              <el-input v-model="form.major" autocomplete="off">
              </el-input>
               </el-form-item>

            <el-form-item label="department" :label-width="formLabelWidth">
              <el-input v-model="form.department" autocomplete="off">
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
  
          <el-form :model="form">

            <el-form-item label="name" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            
            <el-form-item label="age" :label-width="formLabelWidth">
              <el-input v-model="form.age" autocomplete="off">
              </el-input>
             </el-form-item>

            <el-form-item label="sex" :label-width="formLabelWidth">
              <el-input v-model="form.sex" autocomplete="off">
              </el-input>
             </el-form-item>

            <el-form-item label="major" :label-width="formLabelWidth">
              <el-input v-model="form.major" autocomplete="off">
              </el-input>
               </el-form-item>

            <el-form-item label="department" :label-width="formLabelWidth">
              <el-input v-model="form.department" autocomplete="off">
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
        num:9,
        form:{
          id:"-1",
          name:"",
          sex:"",
          age:"",
          major:"",
          department:"",
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
</style>

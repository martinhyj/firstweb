<!--
 * @Author: your name
 * @Date: 2021-03-09 12:28:38
 * @LastEditTime: 2021-03-10 10:25:53
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /t_fronted/src/views/Update.vue
-->



<template>

  <el-table
    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%">

    <el-table-column
      label="Date"
      prop="date">
    </el-table-column>
    <el-table-column
      label="Name"
      prop="name">
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
          @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
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
              <el-button type="primary" @click="handleEdit(scope.$index, scope.row)">确 定</el-button>
            </span>
          </template>
  
        </el-dialog>
        
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
      </template>
      
    </el-table-column>

  </el-table>

</template>

<script>
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }],
        search: '',
        dialogFormVisible:false,
        formLabelWidth:'120px',
        form:{
          name:"李涛",
          sex:"男",
          age:"21",
          major:"软工",
          department:"机缘",
        }
      }
    },
    methods: {
      handleEdit(index,row) {
        this.dialogFormVisible=true;
        this.form.name="杨文彪",
        console.log(index,row);
      },
      handleDelete(index,row) {
        console.log(index, row);
      }
    },
  }
</script>

<style>

</style>

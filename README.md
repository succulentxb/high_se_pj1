## 实验报告

### 程序实现部分
本次实验使用了`python`实现了一个简单的`RESTful API`程序  
程序基于`flask`框架实现，实现了增删改查四个接口
1. 增加学生接口  
    - path: /api/v1/student
    - method: POST
    - body:
    ```json
    {
      "studentId":  1,
      "name": "Mike",
      "department": "Software School",
      "major": "Software Engineering"
    }
    ```
    - response:  
    - Success
    - Invalid Param
    - Student Exist

2. 查询学生接口
    - path: /api/v1/student
    - method: GET
    - response: 
    ```json
    [
        {
          "studentId":  1,
          "name": "Mike",
          "department": "Software School",
          "major": "Software Engineering"
        },
        {...}
    ]
    ```

3. 更新学生接口  
    - path: /api/v1/student
    - method: PUT
    - body:
    ```json
    {
      "studentId":  1,
      "name": "Mike",
      "department": "Software School",
      "major": "Software Engineering"
    }
    ```
    - response:  
    - Success
    - Invalid Param
    - Student Not Exist
 
4. 删除学生接口  
    - path: /api/v1/student
    - method: DELETE
    - body:
    ```json
    {"studentId":  1}
    ```
    - response:  
        - Success
        - Invalid Param
        - Student Not Exist

## 服务部署部分
因为改用了`python`技术栈，所以改写了阿里云效平台提供的`Dockerfile`和`prepare.sh`文件，
使用了`python:3.6`镜像为基础创建镜像，并且对启动文件做了调整
 
<script>
    export default {
        data() {
            return {
                username : '',
                password1: '',
                password2: '',
                email: ''

            }
        },
        methods: {
            async create_user(){
                if(this.username !== '' 
                && this.password1 !== ''
                && this.password2 !== ''
                && this.email !== ''){
                    if(confirm("회원가입을 하시겠습니까?")) {     
                        let body = {
                            username : this.username,
                            password1 : this.password1,
                            password2 : this.password2,
                            email : this.email
                        }
                        body = JSON.stringify(body)

                        let url = "http://127.0.0.1:8000/api/user/create"
                        const res = await fetch(url, this.$makeHttp('POST', body))
                        if(res.status == 204) {
                            console.log(res)
                            console.log('suc')
                        }
                    }
                } else {
                    alert("회원 정보를 모두 입력해주세요.")
                }
            }
        }
    }
</script>

<template>
    <div >
        <h5 className="my-3 border-bottom pb-2">회원 가입</h5>
        <div className="mb-3">
            <label for="username">사용자 이름</label>
            <input type="text" className="form-control" id="username" v-model="username">
        </div>
        <div className="mb-3">
            <label for="password1">비밀번호</label>
            <input type="password" className="form-control" id="password1" v-model="password1">
        </div>
        <div className="mb-3">
            <label for="password2">비밀번호 확인</label>
            <input type="password" className="form-control" id="password2" v-model="password2">
        </div>
        <div className="mb-3">
            <label for="email">이메일</label>
            <input type="text" className="form-control" id="email" v-model="email">
        </div>
        <button className="btn btn-primary" @click="create_user">생성하기</button>
    </div>
</template>
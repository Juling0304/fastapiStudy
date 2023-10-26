<script>
    export default {
        data() {
            return {
                subject: "",
                content: "",
            }
        },
        async mounted() {
        },
        methods: {
            async write_posts() {
                if(this.subject !== '' && this.content !== ''){
                    if(confirm("게시물을 작성하시겠습니까?")) {     
                        let body = {
                            subject : this.subject,
                            content : this.content
                        }
                        body = JSON.stringify(body)

                        let url = "http://127.0.0.1:8000/api/board/posts/create"
                        const res = await fetch(url, this.$makeHttp('POST', body))
                        if(res.status == 204) {
                            console.log(res)
                            console.log('suc')
                        }

                    }
                } else {
                    alert("게시물 제목, 내용을 작성해주세요")
                }
            }
        }
    }
</script>

<template>
    <div className="flex items-center justify-center bg-white border-t-4 border-green-500">
        <div className='w-3/4 mt-10 p-6 bg-green-100 rounded-md drop-shadow-md'>
            <div className='p-6 bg-white rounded-md '>
                <div className='my-5'>
                    <span className='font-bold text-2xl'>글 제목 : </span>
                    <input 
                        type="text"
                        className='w-full mt-2 text-2xl p-2 border rounded-md focus:border-green-400 focus:ring-green-300 focus:outline-none focus:ring focus:ring-opacity-40'
                        placeholder="제목을 입력하세요."
                        v-model="subject">
                </div>
                <div className='my-5'>
                    <span className='font-bold text-2xl'>내용 : </span>
                    <textarea 
                        id="content"
                        className='w-full mt-2 p-2 min-h-[150px] border rounded-md focus:border-green-400 focus:ring-green-300 focus:outline-none focus:ring focus:ring-opacity-40'
                        placeholder="내용을 입력하세요."
                        v-model="content">
                    </textarea>
                </div>
                <button
                    @click="write_posts()"
                    className="mx-1 py-2 px-3 bg-red-200 hover:bg-red-400 text-black-900 hover:text-black-800 rounded transition duration-300">
                    작성
                </button>
                <router-link to="/board" className="mx-1 py-2 px-3 bg-red-200 hover:bg-red-400 text-black-900 hover:text-black-800 rounded transition duration-300">리스트</router-link>       
            </div>
        </div>
    </div>
</template>



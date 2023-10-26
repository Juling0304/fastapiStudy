<script>
    export default {
        data() {
            return {
                posts : { replys: [] },
                reply : ''
            }
        },
        async mounted() {
            await Promise.all([
                this.getPosts()
            ])
        },
        methods: {
            async getPosts() {
                let url = "http://127.0.0.1:8000/api/board/posts/detail/" + this.$route.params.posts_id
                const res = await fetch(url, this.$makeHttp('GET'))

                if(res.status === 200) {
                    this.posts = await res.json()
                }
            },
            async write_reply() {
                if(this.reply !== ''){
                    if(confirm("답변을 작성하시겠습니까?")) {     
                        let body = {
                            posts_id : Number(this.$route.params.posts_id),
                            content : this.reply
                        }
                        body = JSON.stringify(body)

                        let url = "http://127.0.0.1:8000/api/board/reply/create"
                        const res = await fetch(url, this.$makeHttp('POST', body))
                        if(res.status == 204) {
                            this.getPosts()
                            this.reply = ''
                        }

                    }
                } else {
                    alert("답변 내용을 작성해주세요")
                }
            }
        }
    }
</script>

<template>
    <div className="flex items-center justify-center bg-white border-t-4 border-green-500">
        <div className="border-collapse border border-green-400 w-3/4 mt-10 shadow-md">
            <div className='pl-8 py-5  font-bold text-2xl border-b-2 border-green-100'>{{ posts.subject }}</div>
            <div className='pl-8 py-5 border-b-2 border-green-100 whitespace-pre-wrap'>{{ posts.content }}</div>
            <div className='flex pl-5 py-2 justify-end'>
                <div className='m-2 p-2 border border-red-100 text-xs min-w-[90px]'>
                    <p>작성자 : </p>
                    <p></p>
                </div>
                <div className='m-2 p-2 border border-red-100 text-xs'>
                    <p>수정일 : </p>
                    <p></p> 
                </div>
                <div className='m-2 p-2 border border-red-100 text-xs'>
                    <p>등록일 : </p>
                    <p>{{  posts.create_date }}</p>
                </div>
            </div>
        </div>
    </div>


    <div v-if="posts.replys.length > 0" className="flex items-center justify-center mb-2">
        <div className="border-collapse border border-green-400 w-3/4 shadow-md p-2">
            <div v-for="(reply,index) in posts.replys" className='text-xs border-b-2 border-green-100'>
                <div className='mb-2'>답변 : </div>
                <div className="flex mb-2">
                    <div className='w-5/6'>{{ reply.content }}</div>
                    <div>작성자 : </div>
                </div>
            </div>
        </div>
    </div>

    <div className="flex items-center justify-center">
        <div className="border-collapse border border-green-400 w-3/4 shadow-md p-2">
            <div className='mb-2'>내용 : </div>
            <div className="flex items-center justify-center mb-2">
                <textarea id="reply" v-model="reply" className='w-full border-2 border-green-100'></textarea>
            </div>
            <button @click="write_reply()" className="mx-1 py-2 px-3 bg-red-200 hover:bg-red-400 text-black-900 hover:text-black-800 rounded transition duration-300">댓글 작성</button>
        </div>
    </div>
</template>



<script>
    export default {
        data() {
            return {
                postsList : [],
                total: 0,
                page: 1,
                limit: 10,
                pagination: []
            }
        },
        async mounted() {
            await Promise.all([
                this.getPostsList()
            ])
        },
        methods: {
            async getPostsList() {
                let url = "http://127.0.0.1:8000/api/board/posts/list"

                url += "?" + new URLSearchParams({
                    page: this.page,
                    limit: this.limit
                })

                const res = await fetch(url, this.$makeHttp('GET'))

                if(res.status === 200) {
                    let data = await res.json()
                    console.log(data)
                    this.postsList = data.posts_list
                    this.total = data.total

                    this.makePagination()
                }
            },
            makePagination() {
                if (this.total !== 0){
                    let tmp = []
                    for(let i = 1; i <= Math.ceil(this.total / this.limit); i++) {
                        tmp.push(i)
                    }
                    this.pagination = tmp
                }
            },
            clickPagination(event){
                const {
                    currentTarget: { value, id },
                } = event

                if(id === 'prev'){
                    if(this.page !== 1){
                        this.page = this.page - 1
                    }
                } else if(id === 'next'){
                    if(this.page !== Math.ceil(this.total / this.limit)){
                        this.page = this.page + 1
                    }
                } else {
                    this.page = (value * 1)
                }

                this.getPostsList()
            }
        },
    }
</script>

<template>
    <div className="flex items-center justify-center bg-white border-t-4 border-green-500">
        <div className="table border-collapse border border-green-400 w-5/6 mt-10 shadow-md">
            <table className='w-full'>
                <thead className='bg-green-50'>
                    <tr>
                        <th className='w-[20%]'>No.</th>
                        <th className='w-[30%]'>제목</th>
                        <th className='w-[20%]'>글쓴이</th>
                        <th className='w-[20%]'>작성일</th>
                        <th className='w-[10%]'>추천수</th>
                    </tr>
                </thead>
                <tbody>

                    <tr v-for="(posts, index) in postsList" className='border-t-2 border-gray-100 hover:bg-green-100' key={item.id}>
                        <td className='text-center'>{{ total - (limit * (page - 1)) - index }}</td>
                        <td className='text-center'>
                            <router-link :to="{ name: 'posts', params: { posts_id: posts.id } }">{{ posts.subject }}</router-link>
                            <span v-if="posts.replys.length > 0" className="text-sm text-red-400 ml-2">{{ posts.replys.length }}</span>
                        </td>
                        <td className='text-center'></td>
                        <td className='text-center'>{{ posts.create_date }}</td>
                        <td className='text-center text-red-400'></td>
                    </tr>

                </tbody>
            </table>
        </div>
    </div>
    <div v-show="total > 0" className='mt-5 flex items-center justify-center'>
        <button @click="clickPagination" id="prev" className='mx-2'>{{ '<' }}</button>
            <button v-for="(each, item) in pagination" @click="clickPagination" className='mx-2' :value="each" :key="each" :class="[each == page ? 'text-green-400' : '' ]">{{ each }}</button>
        <button @click="clickPagination" id="next" className='mx-2'>{{ '>' }}</button>
    </div>
    <div className="flex items-center justify-center">
        <div className="w-5/6">
            <router-link to="/board/posts/write" className="py-2 px-3 bg-red-200 hover:bg-red-400 text-black-900 hover:text-black-800 rounded transition duration-300">글쓰기</router-link>       
        </div>
    </div>
</template>



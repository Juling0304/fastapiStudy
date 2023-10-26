export default {

    install(Vue) {
        Vue.config.globalProperties.$makeHttp = (method = null, body = null) => {

            // GET
            if(method == 'GET'){
                const headers = { 'Content-Type': 'application/json' }
                return {
                    method: 'GET',
                    headers: headers,
                }
            }

            // POST
            if(method == 'POST'){
                const headers = { 'Content-Type': 'application/json' }

                if (body === null) {
                    return {
                        method: 'POST',
                        headers: headers,
                    }
                } else {
                    return {
                        method: 'POST',
                        headers: headers,
                        body: body
                    }
                }
            }

        }

    }
}
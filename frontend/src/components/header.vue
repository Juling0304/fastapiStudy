<script>

</script>
<template>
    <nav className="bg-gray-100">
        <div className="max-w-6xl mx-auto px-4">
            <div className="flex justify-between">
                <div className="flex space-x-4">
                    <div>
                        <div className="flex items-center py-5 px-2 text-gray-700">
                            <span className="font-bold">Home</span>
                        </div>
                    </div>
                    <div className="flex items-center space-x-1">
                        <div>
                            게시판
                        </div>
                    </div>
                </div>
                <div className="hidden md:flex items-center space-x-1">
                    <button className="py-5 px-3">
                        Log out
                    </button>
                    <span className="py-2 px-3 bg-green-200 hover:bg-green-400 text-black-900 hover:text-black-800 rounded transition duration-300">
                        name
                    </span>
                </div>
                <div className="md:hidden flex items-center">
                    <button>
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-6 w-6"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={2}
                                d="M4 6h16M4 12h16M4 18h16"
                            />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </nav>
</template>
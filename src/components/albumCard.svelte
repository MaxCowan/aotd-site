<script>
export let album;
    
</script>
<!-- TODO use an href when focused album view component is done -->

<div class="group relative h-[260px] w-[260px] rounded-md shadow-md hover:shadow-2xl over:blur-sm flex items-center transition duration-400" >
    <img src="https://p1.hiclipart.com/preview/321/1024/864/itunes-13-el-capitan-apple-itunes-logo.jpg" alt="" class="z-0 absoluterounded-md object-cover w-full h-full group-hover:blur-md transition duration-500"/>
    <div class="z-1 absolute opacity-0 group-hover:opacity-100 bg-gradient-to-t from-black to-transparent transition duration-500 absolute w-full h-full text-black rounded-md"></div>
    <div class="z-2 absolute opacity-0 group-hover:opacity-100 transition duration-500 absolute py-2.5 bottom-1.5 left-4 right-4 inset-x-0 text-white rounded-md text-lg text-center font-bold tracking-wide leading-6 ">{album.name}</div>
</div>

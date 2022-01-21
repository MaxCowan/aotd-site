<script>
export let album;
    
</script>
<!-- TODO use an href when focused album view component is done -->

<div class="group relative h-[260px] w-[260px] rounded-md group-hover:shadow-2xl group-hover:scale-[1.05] flex items-center transition duration-400" >
    <img src="https://upload.wikimedia.org/wikipedia/en/9/9b/Tame_Impala_-_Currents.png?1642732008806" alt="" class="absolute rounded-lg drop-shadow-md w-full h-full group-hover:blur-sm group-hover:scale-[1.05] transition duration-500"/>
    <div class="z-1 absolute opacity-0 group-hover:opacity-100 group-hover:scale-[1.05] bg-gradient-to-t from-black to-transparent transition duration-500 absolute w-full h-full rounded-md"></div>
    <div class="z-2 absolute opacity-0 group-hover:opacity-100 group-hover:-translate-y-3 transition duration-500 absolute py-2.5 bottom-0 left-4 right-4 inset-x-0 text-white text-lg text-center antialiased font-bold tracking-wide leading-6 ">{album.name}</div>
</div>

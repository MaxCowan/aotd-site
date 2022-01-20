<script>
export let album;
    
</script>
<!-- TODO use an href when focused album view component is done -->

<div class="list-none h-[260px] w-[260px] p-6 bg-contain bg-[url('https://p1.hiclipart.com/preview/321/1024/864/itunes-13-el-capitan-apple-itunes-logo.jpg')] text-black text-center font-extrabold rounded-md shadow-md hover:shadow-2xl over:blur-sm flex flex-col items-center" >
    <h2 class="uppercase text-2xl">{album.name}<br></h2>
    <h2 class="uppercase text-2xl">-------<br>{album.artist}</h2>
</div>
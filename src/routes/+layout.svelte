<script>
import "../global.css";
import Nav from "../components/Nav.svelte";
</script>

<div class="layout-container">
    <Nav />
    <div class="content">
        <slot></slot>
    </div>
</div>

<style>
.layout-container {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    padding: 30px;
}

.content {
    flex: 1;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    font-family: inherit;
}
</style>

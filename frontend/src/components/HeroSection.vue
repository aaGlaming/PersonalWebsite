<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})

function go(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <section id="home" class="hero">
    <div class="hd-container grid">
      <div class="left">
        <span class="hd-sticker hello">Hi, 我是</span>
        <h1 class="name">{{ profile.name || '陆杨磊' }}</h1>
        <h2 class="title">
          {{ profile.title || '数据分析 · 数据挖掘' }}
          <span class="bang">!</span>
        </h2>
        <p class="slogan">"{{ profile.slogan }}"</p>
        <div class="cta">
          <el-button type="primary" size="large" @click="go('projects')">
            看看我的项目 →
          </el-button>
          <el-button size="large" @click="go('contact')">联系我</el-button>
        </div>
        <p class="contact-hint">
          📞 {{ profile.phone }} · ✉️ {{ profile.email }}
        </p>
      </div>

      <div class="right">
        <div class="avatar-frame">
          <span class="corner tl"></span>
          <span class="corner tr"></span>
          <span class="corner bl"></span>
          <span class="corner br"></span>
          <div class="avatar wobbly-md">
            <span class="face">数据分析<br />打工人</span>
          </div>
        </div>
        <!-- 手绘箭头指向 CTA（仅桌面端） -->
        <svg class="arrow hd-bounce" viewBox="0 0 120 90" fill="none">
          <path
            d="M100 8 C 70 20, 50 40, 28 66 M28 66 l 4 -18 M28 66 l 18 -2"
            stroke="#2d5da1"
            stroke-width="3"
            stroke-linecap="round"
            stroke-dasharray="7 6"
          />
        </svg>
        <!-- 弹跳装饰圆 -->
        <span class="deco-circle hd-bounce"></span>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  padding: 96px 24px 72px;
}
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 48px;
  align-items: center;
}
@media (min-width: 768px) {
  .grid { grid-template-columns: 1.2fr 1fr; }
}
.hello {
  font-size: 20px;
  margin-bottom: 8px;
}
.name {
  font-size: 64px;
  margin: 12px 0 0;
}
.title {
  font-size: 34px;
  margin: 4px 0 0;
  color: var(--hd-blue);
}
.bang {
  display: inline-block;
  color: var(--hd-accent);
  transform: rotate(12deg);
  transition: transform 0.2s ease;
}
.bang:hover {
  transform: rotate(-12deg) scale(1.3);
}
.slogan {
  font-size: 20px;
  margin: 20px 0 0;
  color: rgba(45, 45, 45, 0.75);
}
.cta {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 28px;
}
.contact-hint {
  margin-top: 20px;
  color: rgba(45, 45, 45, 0.55);
  font-size: 16px;
}
.right {
  position: relative;
  display: flex;
  justify-content: center;
}
.avatar-frame {
  position: relative;
  padding: 18px;
}
.corner {
  position: absolute;
  width: 34px;
  height: 34px;
}
.corner.tl {
  top: 0; left: 0;
  border-top: 4px solid var(--hd-fg);
  border-left: 4px solid var(--hd-fg);
  border-top-left-radius: 60% 70%;
}
.corner.tr {
  top: 0; right: 0;
  border-top: 4px solid var(--hd-fg);
  border-right: 4px solid var(--hd-fg);
  border-top-right-radius: 70% 60%;
}
.corner.bl {
  bottom: 0; left: 0;
  border-bottom: 4px solid var(--hd-fg);
  border-left: 4px solid var(--hd-fg);
  border-bottom-left-radius: 70% 60%;
}
.corner.br {
  bottom: 0; right: 0;
  border-bottom: 4px solid var(--hd-fg);
  border-right: 4px solid var(--hd-fg);
  border-bottom-right-radius: 60% 70%;
}
.avatar {
  width: 220px;
  height: 220px;
  background: var(--hd-postit);
  border: 3px solid var(--hd-border);
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  transform: rotate(1.5deg);
}
.face {
  font-family: var(--font-marker);
  font-size: 34px;
  text-align: center;
  line-height: 1.4;
  transform: rotate(-2deg);
}
.arrow {
  position: absolute;
  left: -60px;
  bottom: -30px;
  width: 110px;
  transform: rotate(-10deg);
}
.deco-circle {
  position: absolute;
  top: -26px;
  right: 8px;
  width: 34px;
  height: 30px;
  background: var(--hd-accent);
  border: 2px solid var(--hd-border);
  border-radius: 48% 55% 52% 46%;
  opacity: 0.9;
}
@media (max-width: 767px) {
  .arrow, .deco-circle { display: none; }
  .name { font-size: 48px; }
  .title { font-size: 27px; }
}
</style>

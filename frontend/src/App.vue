<script setup>
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import AboutSection from './components/AboutSection.vue'
import SkillsSection from './components/SkillsSection.vue'
import ProjectsSection from './components/ProjectsSection.vue'
import EducationSection from './components/EducationSection.vue'
import ContactSection from './components/ContactSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <NavBar />
  <main>
    <HeroSection />
    <AboutSection />
    <SkillsSection />
    <ProjectsSection />
    <EducationSection />
    <ContactSection />
  </main>
  <FooterSection />
  <el-backtop :right="28" :bottom="28" />
</template>

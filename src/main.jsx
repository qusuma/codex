import React, { useEffect, useState } from 'react'
import { createRoot } from 'react-dom/client'
import { AnimatePresence, motion } from 'motion/react'
import './styles.css'

const swapWords = ['posters', 'stories', 'websites', 'videos', 'explainers']

const floatingCards = [
  { label: 'Prompt', icon: '✏️', text: 'A moon mouse paints stars', position: 'md:left-2 md:top-12' },
  { label: 'Design', icon: '🎨', text: 'Pastel layouts bloom', position: 'md:right-0 md:top-24' },
  { label: 'Animate', icon: '✨', text: 'Gentle motion magic', position: 'md:left-8 md:bottom-24' },
  { label: 'Publish', icon: '🚀', text: 'Share a tiny world', position: 'md:right-8 md:bottom-8' },
]

const steps = [
  {
    title: 'Whisper an idea',
    text: 'Start with a tiny prompt, a classroom concept, or a half-dreamed character.',
    icon: '🌙',
  },
  {
    title: 'Shape the scene',
    text: 'Choose storybook palettes, poster layouts, playful diagrams, and soft motion styles.',
    icon: '🧁',
  },
  {
    title: 'Let it come alive',
    text: 'Export charming animated explainers, social videos, web moments, or print-ready art.',
    icon: '🪄',
  },
]

const galleryItems = [
  { title: 'Cloud Garden Poster', tag: 'storybook poster', gradient: 'from-blush via-cream to-sky', emoji: '☁️' },
  { title: 'Mushroom Lab Notes', tag: 'cute science art', gradient: 'from-butter via-cream to-peach', emoji: '🍄' },
  { title: 'Tiny Rocket Lesson', tag: 'animated explainer', gradient: 'from-sky via-cream to-lilac', emoji: '🚀' },
  { title: 'Sleepy Forest Site', tag: 'gentle website', gradient: 'from-lilac via-cream to-blush', emoji: '🦊' },
  { title: 'Bee Math Motion', tag: 'learning video', gradient: 'from-butter via-peach to-cream', emoji: '🐝' },
  { title: 'Ocean Story Cards', tag: 'visual narrative', gradient: 'from-sky via-blush to-cream', emoji: '🐚' },
]

const tools = ['Storyboard maker', 'Palette spells', 'Poster canvas', 'Motion presets', 'Science doodles', 'Export nook']

function WordSwap() {
  const [index, setIndex] = useState(0)

  useEffect(() => {
    const timer = window.setInterval(() => {
      setIndex((current) => (current + 1) % swapWords.length)
    }, 1800)

    return () => window.clearInterval(timer)
  }, [])

  return (
    <span className="relative inline-flex min-w-[8.5rem] justify-center overflow-hidden rounded-full bg-white/70 px-4 py-1 text-lilac shadow-card ring-1 ring-white/80 sm:min-w-[11rem]">
      <AnimatePresence mode="wait">
        <motion.span
          key={swapWords[index]}
          initial={{ y: 24, opacity: 0, rotate: -3 }}
          animate={{ y: 0, opacity: 1, rotate: 0 }}
          exit={{ y: -24, opacity: 0, rotate: 3 }}
          transition={{ duration: 0.42, ease: 'easeOut' }}
          className="inline-block"
        >
          {swapWords[index]}
        </motion.span>
      </AnimatePresence>
    </span>
  )
}

function BlobBackdrop() {
  return (
    <div className="pointer-events-none absolute inset-0 overflow-hidden" aria-hidden="true">
      <div className="blob blob-one" />
      <div className="blob blob-two" />
      <div className="blob blob-three" />
      <div className="sparkle sparkle-one">✦</div>
      <div className="sparkle sparkle-two">✧</div>
      <div className="sparkle sparkle-three">✦</div>
      <div className="sparkle sparkle-four">✧</div>
    </div>
  )
}

function Hero() {
  return (
    <section className="relative isolate min-h-screen overflow-hidden px-4 py-6 sm:px-6 lg:px-8">
      <BlobBackdrop />
      <nav className="relative z-10 mx-auto flex max-w-6xl items-center justify-between rounded-full bg-white/45 px-4 py-3 shadow-card ring-1 ring-white/70 backdrop-blur md:px-6">
        <a href="#top" className="flex items-center gap-2 font-display text-lg font-black text-ink">
          <span className="grid h-10 w-10 place-items-center rounded-full bg-butter shadow-card">🖍️</span>
          CozyCanvas AI
        </a>
        <a href="#examples" className="hidden rounded-full bg-ink px-4 py-2 text-sm font-bold text-cream shadow-card transition hover:-translate-y-0.5 sm:inline-block">
          Explore
        </a>
      </nav>

      <div id="top" className="relative z-10 mx-auto grid max-w-6xl items-center gap-10 pb-16 pt-12 md:grid-cols-[1.05fr_0.95fr] md:pb-24 md:pt-20">
        <motion.div initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }}>
          <p className="mb-4 inline-flex rounded-full bg-white/65 px-4 py-2 text-sm font-extrabold uppercase tracking-[0.18em] text-ink/70 shadow-card ring-1 ring-white/80">
            A cozy AI creative studio
          </p>
          <h1 className="font-display text-5xl font-black leading-[0.95] tracking-tight text-ink sm:text-6xl lg:text-7xl">
            Turn tiny ideas into beautiful animated worlds for <WordSwap />
          </h1>
          <p className="mt-6 max-w-xl text-lg leading-8 text-ink/75 sm:text-xl">
            Make storybook posters, cute science art, and animated explainers with a warm canvas, friendly tools, and just enough sparkle.
          </p>
          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <a href="#create" className="rounded-full bg-ink px-7 py-4 text-center font-black text-cream shadow-soft transition hover:-translate-y-1 hover:shadow-card">
              Start Creating
            </a>
            <a href="#examples" className="rounded-full bg-white/70 px-7 py-4 text-center font-black text-ink shadow-card ring-1 ring-white/80 transition hover:-translate-y-1">
              See Examples
            </a>
          </div>
        </motion.div>

        <div className="relative mx-auto h-[34rem] w-full max-w-md md:max-w-none">
          <motion.div
            initial={{ opacity: 0, scale: 0.92, rotate: -2 }}
            animate={{ opacity: 1, scale: 1, rotate: 0 }}
            transition={{ duration: 0.8, delay: 0.15 }}
            className="absolute inset-x-4 top-14 rounded-[2.5rem] bg-white/78 p-5 shadow-soft ring-1 ring-white/80 backdrop-blur md:inset-x-12"
          >
            <div className="rounded-[2rem] bg-gradient-to-br from-blush via-cream to-sky p-5">
              <div className="flex items-center gap-2">
                <span className="h-3 w-3 rounded-full bg-blush" />
                <span className="h-3 w-3 rounded-full bg-butter" />
                <span className="h-3 w-3 rounded-full bg-sky" />
              </div>
              <div className="mt-8 grid place-items-center rounded-[1.6rem] bg-white/55 px-4 py-12 text-center shadow-card">
                <motion.div animate={{ y: [0, -10, 0] }} transition={{ duration: 5, repeat: Infinity, ease: 'easeInOut' }} className="text-7xl">
                  🐰
                </motion.div>
                <p className="mt-4 font-display text-2xl font-black text-ink">Moon Bunny Observatory</p>
                <p className="mt-2 text-sm font-semibold text-ink/65">A science poster that twinkles softly.</p>
              </div>
            </div>
          </motion.div>

          {floatingCards.map((card, cardIndex) => (
            <motion.div
              key={card.label}
              initial={{ opacity: 0, y: 18 }}
              animate={{ opacity: 1, y: [0, -10, 0] }}
              transition={{
                opacity: { duration: 0.4, delay: 0.45 + cardIndex * 0.12 },
                y: { duration: 4 + cardIndex * 0.4, repeat: Infinity, ease: 'easeInOut', delay: cardIndex * 0.3 },
              }}
              className={`absolute ${card.position} rounded-3xl bg-white/82 p-4 shadow-card ring-1 ring-white/80 backdrop-blur max-md:relative max-md:mb-3 max-md:ml-auto max-md:mr-2 max-md:top-auto max-md:w-[78%] md:w-44`}
            >
              <div className="flex items-center gap-3">
                <span className="grid h-11 w-11 place-items-center rounded-2xl bg-cream text-xl shadow-card">{card.icon}</span>
                <div>
                  <p className="font-display text-lg font-black text-ink">{card.label}</p>
                  <p className="text-xs font-semibold text-ink/60">{card.text}</p>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

function Process() {
  return (
    <section className="px-4 py-16 sm:px-6 lg:px-8" id="create">
      <div className="mx-auto max-w-6xl">
        <div className="text-center">
          <p className="text-sm font-black uppercase tracking-[0.2em] text-lilac">Three tiny steps</p>
          <h2 className="mt-3 font-display text-4xl font-black text-ink sm:text-5xl">From seedling thought to animated tale</h2>
        </div>
        <div className="mt-10 grid gap-5 md:grid-cols-3">
          {steps.map((step, index) => (
            <motion.article
              key={step.title}
              initial={{ opacity: 0, y: 26 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-80px' }}
              transition={{ duration: 0.5, delay: index * 0.08 }}
              className="rounded-[2rem] bg-white/72 p-6 shadow-card ring-1 ring-white/80 backdrop-blur"
            >
              <span className="grid h-16 w-16 place-items-center rounded-3xl bg-gradient-to-br from-butter to-peach text-3xl shadow-card">{step.icon}</span>
              <p className="mt-6 font-display text-2xl font-black text-ink">{step.title}</p>
              <p className="mt-3 leading-7 text-ink/70">{step.text}</p>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  )
}

function Gallery() {
  return (
    <section className="px-4 py-16 sm:px-6 lg:px-8" id="examples">
      <div className="mx-auto max-w-6xl rounded-[2.5rem] bg-white/55 p-4 shadow-soft ring-1 ring-white/80 backdrop-blur sm:p-8">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-sm font-black uppercase tracking-[0.2em] text-peach">Gallery preview</p>
            <h2 className="mt-3 font-display text-4xl font-black text-ink sm:text-5xl">Little worlds waiting to be made</h2>
          </div>
          <p className="max-w-sm text-ink/70">Preview cards for posters, animated explainers, science visuals, story scenes, and cozy web moments.</p>
        </div>
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {galleryItems.map((item, index) => (
            <motion.article
              key={item.title}
              initial={{ opacity: 0, scale: 0.94 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true, margin: '-60px' }}
              transition={{ duration: 0.45, delay: index * 0.04 }}
              whileHover={{ y: -6, rotate: index % 2 === 0 ? -1 : 1 }}
              className={`min-h-56 rounded-[2rem] bg-gradient-to-br ${item.gradient} p-5 shadow-card ring-1 ring-white/80`}
            >
              <div className="flex h-full flex-col justify-between rounded-[1.5rem] bg-white/45 p-5 backdrop-blur-sm">
                <span className="text-5xl">{item.emoji}</span>
                <div>
                  <p className="font-display text-2xl font-black text-ink">{item.title}</p>
                  <p className="mt-1 text-sm font-bold uppercase tracking-[0.16em] text-ink/55">{item.tag}</p>
                </div>
              </div>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  )
}

function Tools() {
  return (
    <section className="px-4 py-16 sm:px-6 lg:px-8">
      <div className="mx-auto grid max-w-6xl gap-8 rounded-[2.5rem] bg-cream/70 p-6 shadow-soft ring-1 ring-white/80 md:grid-cols-[0.9fr_1.1fr] md:p-10">
        <div>
          <p className="text-sm font-black uppercase tracking-[0.2em] text-sky">Studio tools</p>
          <h2 className="mt-3 font-display text-4xl font-black text-ink sm:text-5xl">Everything feels like a craft table</h2>
          <p className="mt-5 leading-8 text-ink/70">
            Pick a mood, arrange a scene, sprinkle in motion, and export without leaving the cozy canvas.
          </p>
        </div>
        <div className="grid gap-3 sm:grid-cols-2">
          {tools.map((tool, index) => (
            <motion.div
              key={tool}
              initial={{ opacity: 0, x: 18 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.4, delay: index * 0.05 }}
              className="rounded-3xl bg-white/72 p-5 font-display text-xl font-black text-ink shadow-card ring-1 ring-white/80"
            >
              <span className="mr-2 text-2xl">✿</span>
              {tool}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

function CTA() {
  return (
    <section className="px-4 py-16 pb-24 sm:px-6 lg:px-8">
      <motion.div
        initial={{ opacity: 0, y: 24 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.55 }}
        className="relative mx-auto max-w-5xl overflow-hidden rounded-[2.5rem] bg-ink px-6 py-14 text-center shadow-soft sm:px-10"
      >
        <div className="absolute -left-10 -top-10 h-36 w-36 rounded-full bg-lilac/40 blur-2xl" />
        <div className="absolute -bottom-12 -right-8 h-40 w-40 rounded-full bg-peach/50 blur-2xl" />
        <div className="relative">
          <p className="text-5xl">🌈</p>
          <h2 className="mt-4 font-display text-4xl font-black text-cream sm:text-5xl">Ready to open the tiny studio door?</h2>
          <p className="mx-auto mt-4 max-w-2xl leading-8 text-cream/75">
            Bring a lesson, a poster idea, or a sleepy character. CozyCanvas AI turns it into something polished, playful, and alive.
          </p>
          <a href="#top" className="mt-8 inline-flex rounded-full bg-butter px-8 py-4 font-black text-ink shadow-card transition hover:-translate-y-1">
            Start Creating
          </a>
        </div>
      </motion.div>
    </section>
  )
}

function App() {
  return (
    <main>
      <Hero />
      <Process />
      <Gallery />
      <Tools />
      <CTA />
    </main>
  )
}

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

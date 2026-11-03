# -*- coding: utf-8 -*-
"""
Generator for Shubhankar Negi's Interactive Portfolio
Inspire by piergorelli.com with rich full-stack developer micro-interactions,
hacker text decrypt animations, compile loader, terminal REPL dock, REST playground,
OpenCV filter studio, and live system telemetry.
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="en" data-theme="dark" data-motion="showcase">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Shubhankar Negi — Full Stack Developer | L&amp;T</title>
    <meta name="description" content="Portfolio of Shubhankar Negi, Full Stack Developer at Larsen &amp; Toubro (L&amp;T), Pune. Resilient enterprise web services, Python automation, and computer vision systems.">
    <link rel="canonical" href="https://shubhankar.dev/">
    <meta name="theme-color" content="#0b0b0c">

    <!-- Fonts: Geist & Geist Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800;900&family=Geist+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <!-- FontAwesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <style>
        /* ===== CSS RESET & DESIGN TOKENS ===== */
        :root {
            /* Light Theme (Warm Paper / Swiss Editorial) */
            --bg: #f4f4f0;
            --bg-raised: #ecece6;
            --bg-surface: #ffffff;
            --ink: #0e0e0d;
            --muted: #65655f;
            --line: rgba(14, 14, 13, 0.14);
            --line-strong: rgba(14, 14, 13, 0.32);
            --control-line: rgba(14, 14, 13, 0.5);
            --accent: #2f5bff;
            --accent-ink: #ffffff;
            --accent-text: #2a52f0;
            --accent-dim: rgba(47, 91, 255, 0.12);
            --success: #10b981;
            --danger: #c02b24;

            --font-sans: "Geist", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: "Geist Mono", ui-monospace, "SF Mono", monospace;

            /* Modular Fluid Typography Scale */
            --step--1: clamp(0.78rem, 0.74rem + 0.18vw, 0.875rem);
            --step-0: clamp(0.96rem, 0.9rem + 0.28vw, 1.125rem);
            --step-1: clamp(1.2rem, 1.08rem + 0.6vw, 1.55rem);
            --step-2: clamp(1.5rem, 1.25rem + 1.25vw, 2.3rem);
            --step-3: clamp(2rem, 1.45rem + 2.8vw, 3.8rem);
            --step-4: clamp(2.8rem, 1.6rem + 5.5vw, 6.5rem);
            --step-5: clamp(3.4rem, 1.2rem + 9.5vw, 10.5rem);

            --gutter: clamp(18px, 3.5vw, 48px);
            --columns: 12;
            --col-gap: clamp(12px, 1.6vw, 28px);
            --section-gap: clamp(84px, 10vw, 160px);

            --dur-1: 0.25s;
            --dur-2: 0.55s;
            --dur-3: 0.9s;
            --ease-out: cubic-bezier(0.25, 1, 0.5, 1);
            --ease-in-out: cubic-bezier(0.76, 0, 0.24, 1);

            color-scheme: light;
        }

        /* Dark Theme (Graphite & Warm Chalk) */
        [data-theme="dark"] {
            --bg: #0b0b0c;
            --bg-raised: #141416;
            --bg-surface: #1a1a1e;
            --ink: #edede7;
            --muted: #8b8b85;
            --line: rgba(237, 237, 231, 0.12);
            --line-strong: rgba(237, 237, 231, 0.3);
            --control-line: rgba(237, 237, 231, 0.45);
            --accent: #3b82f6;
            --accent-ink: #ffffff;
            --accent-text: #60a5fa;
            --accent-dim: rgba(59, 130, 246, 0.15);
            --success: #34d399;
            --danger: #ff6b5e;

            color-scheme: dark;
        }

        /* Base Resets */
        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
            font-size: 16px;
            background-color: var(--bg);
            color: var(--ink);
            transition: background-color var(--dur-1) var(--ease-out), color var(--dur-1) var(--ease-out);
        }

        body {
            font-family: var(--font-sans);
            font-size: var(--step-0);
            line-height: 1.55;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            position: relative;
        }

        a { color: inherit; text-decoration: none; }
        button { font: inherit; color: inherit; background: none; border: none; cursor: pointer; }
        ::selection { background: var(--ink); color: var(--bg); }

        /* ===== 1. COMPILE INTRO PRELOADER (ARCHITECTURAL HUD) ===== */
        .preloader {
            position: fixed;
            inset: 0;
            background: var(--bg);
            z-index: 99999;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: var(--gutter);
            font-family: var(--font-mono);
            transition: opacity 0.7s var(--ease-in-out), transform 0.7s var(--ease-in-out), visibility 0.7s;
        }

        .preloader.is-done {
            opacity: 0;
            transform: translateY(-24px);
            visibility: hidden;
            pointer-events: none;
        }

        .preloader__meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: var(--step--1);
            color: var(--muted);
            border-bottom: 1px solid var(--line);
            padding-bottom: 0.85rem;
        }

        .preloader__center {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 1.75rem;
            max-width: 620px;
            width: 100%;
            margin-inline: auto;
        }

        .preloader__mark {
            width: 96px;
            height: 56px;
            color: var(--ink);
            filter: drop-shadow(0 0 12px var(--accent-dim));
        }

        .preloader__mark path {
            stroke-dasharray: 120;
            stroke-dashoffset: 120;
            animation: drawMonogram 1.6s cubic-bezier(0.65, 0, 0.35, 1) forwards;
        }

        @keyframes drawMonogram {
            to { stroke-dashoffset: 0; }
        }

        /* Terminal boot log window inside preloader */
        .preloader__console {
            width: 100%;
            background: var(--bg-surface);
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: 14px 18px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-size: var(--step--1);
            line-height: 1.6;
            min-height: 120px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        }

        .preloader__log-line {
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--muted);
            opacity: 0;
            transform: translateY(4px);
            transition: opacity 0.25s ease, transform 0.25s ease;
        }

        .preloader__log-line.active {
            opacity: 1;
            transform: translateY(0);
            color: var(--ink);
        }

        .preloader__log-line .tag {
            color: var(--accent-text);
            font-size: 0.72rem;
            padding: 1px 6px;
            background: var(--accent-dim);
            border-radius: 3px;
        }

        /* Progress Bar */
        .preloader__progress-bar-wrap {
            width: 100%;
            height: 4px;
            background: var(--line);
            border-radius: 2px;
            overflow: hidden;
            position: relative;
        }

        .preloader__progress-bar {
            height: 100%;
            width: 0%;
            background: var(--accent);
            transition: width 0.1s linear;
        }

        .preloader__foot {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            font-size: var(--step--1);
            color: var(--muted);
            border-top: 1px solid var(--line);
            padding-top: 0.85rem;
        }

        .preloader__count {
            color: var(--accent-text);
            font-weight: 600;
            font-size: var(--step-0);
        }

        .preloader__skip-btn {
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            background: var(--bg-raised);
            border: 1px solid var(--line);
            padding: 3px 10px;
            border-radius: 4px;
            transition: all 0.2s ease;
        }

        .preloader__skip-btn:hover {
            color: var(--ink);
            border-color: var(--ink);
        }

        /* ===== BLUEPRINT WIREFRAME GRID OVERLAY ===== */
        .blueprint-grid-overlay {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 1000;
            opacity: 0;
            transition: opacity var(--dur-1) var(--ease-out);
            background-image:
                linear-gradient(to right, var(--line) 1px, transparent 1px),
                linear-gradient(to bottom, var(--line) 1px, transparent 1px);
            background-size: 32px 32px;
        }

        body.show-grid .blueprint-grid-overlay { opacity: 1; }

        .hud-dimensions {
            position: fixed;
            bottom: 14px;
            right: 18px;
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            background: var(--bg-raised);
            padding: 4px 10px;
            border: 1px solid var(--line);
            border-radius: 4px;
            z-index: 1001;
            display: none;
            letter-spacing: -0.02em;
        }

        body.show-grid .hud-dimensions { display: block; }

        /* ===== MATRIX DIGITAL RAIN OVERLAY ===== */
        #matrixCanvas {
            position: fixed;
            inset: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 9998;
            opacity: 0;
            transition: opacity 0.4s ease;
        }

        body.matrix-active #matrixCanvas {
            opacity: 0.92;
            pointer-events: auto;
        }

        .matrix-exit-btn {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            background: #00ff66;
            color: #000;
            font-family: var(--font-mono);
            font-weight: 700;
            padding: 8px 16px;
            border-radius: 4px;
            display: none;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(0, 255, 102, 0.4);
        }

        body.matrix-active .matrix-exit-btn { display: block; }

        /* ===== CUSTOM PRECISION CURSOR ===== */
        @media (hover: hover) and (pointer: fine) {
            .tech-cursor {
                position: fixed;
                width: 10px;
                height: 10px;
                background: var(--ink);
                border-radius: 50%;
                pointer-events: none;
                z-index: 99998;
                transform: translate(-50%, -50%);
                transition: transform 0.05s linear, background 0.2s ease, width 0.25s var(--ease-out), height 0.25s var(--ease-out);
            }

            .tech-cursor-follower {
                position: fixed;
                width: 32px;
                height: 32px;
                border: 1px solid var(--control-line);
                border-radius: 50%;
                pointer-events: none;
                z-index: 99997;
                transform: translate(-50%, -50%);
                transition: width 0.25s var(--ease-out), height 0.25s var(--ease-out), border-color 0.2s ease, background 0.2s ease;
            }

            .cursor-action .tech-cursor {
                transform: translate(-50%, -50%) scale(1.6);
                background: var(--accent);
            }

            .cursor-action .tech-cursor-follower {
                width: 48px;
                height: 48px;
                border-color: var(--accent);
                background: var(--accent-dim);
            }
        }

        /* ===== UTILITY STYLES ===== */
        .wrap {
            max-width: 1420px;
            margin-inline: auto;
            padding-inline: var(--gutter);
        }

        .note {
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            letter-spacing: -0.015em;
        }

        .note--ink { color: var(--ink); }
        .note--accent { color: var(--accent-text); }
        .note--success { color: var(--success); }

        .display {
            font-size: var(--step-5);
            letter-spacing: -0.055em;
            line-height: 0.88;
            font-weight: 500;
        }

        .h1 {
            font-size: var(--step-4);
            letter-spacing: -0.045em;
            line-height: 0.95;
            font-weight: 500;
        }

        .h2 {
            font-size: var(--step-2);
            letter-spacing: -0.035em;
            line-height: 1.15;
            font-weight: 500;
        }

        .h3 {
            font-size: var(--step-1);
            letter-spacing: -0.025em;
            line-height: 1.25;
            font-weight: 500;
        }

        .lead {
            font-size: var(--step-1);
            letter-spacing: -0.02em;
            line-height: 1.45;
            color: var(--muted);
        }

        .lead strong, .lead .ink-text {
            color: var(--ink);
            font-weight: 500;
        }

        /* Wireframe Outline Text */
        .outline-text {
            color: transparent;
            -webkit-text-stroke: 1px var(--line-strong);
            user-select: none;
            transition: color var(--dur-1) var(--ease-out);
        }

        .section-head {
            border-top: 1px solid var(--line-strong);
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            gap: 1rem;
            margin-bottom: clamp(48px, 6vw, 96px);
            padding-top: 0.85rem;
            font-family: var(--font-mono);
            font-size: var(--step--1);
        }

        .grid-12 {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            column-gap: var(--col-gap);
        }

        /* Button Architecture */
        .btn {
            --btn-bg: var(--ink);
            --btn-fg: var(--bg);
            background: var(--btn-bg);
            color: var(--btn-fg);
            height: 3.1rem;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            padding-inline: 1.5rem;
            border-radius: 999px;
            font-size: var(--step-0);
            font-weight: 400;
            letter-spacing: -0.015em;
            transition: all var(--dur-1) var(--ease-out);
            border: 1px solid transparent;
            white-space: nowrap;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        }

        .btn--ghost {
            --btn-bg: transparent;
            --btn-fg: var(--ink);
            border-color: var(--line-strong);
        }

        .btn--ghost:hover {
            border-color: var(--ink);
            background: var(--bg-raised);
        }

        .btn .arrow {
            font-family: var(--font-mono);
            transition: transform var(--dur-1) var(--ease-out);
        }

        .btn:hover .arrow { transform: translateX(4px); }

        /* Scramble Text Hover Utility */
        [data-scramble] {
            cursor: default;
        }

        /* Scroll Reveal Effect */
        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(22px);
            transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .reveal-on-scroll.in-view {
            opacity: 1;
            transform: translateY(0);
        }

        /* ===== SITE HEADER & SCROLL RULER ===== */
        .site-header {
            position: fixed;
            inset: 0 0 auto 0;
            height: 4.5rem;
            z-index: 90;
            display: grid;
            grid-template-columns: auto 1fr auto;
            align-items: center;
            gap: 1.5rem;
            background: var(--bg);
            background: color-mix(in srgb, var(--bg) 88%, transparent);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--line);
        }

        /* Calibrated Ruler below Header */
        .scroll-ruler-track {
            position: absolute;
            bottom: -2px;
            left: 0;
            right: 0;
            height: 2px;
            background: transparent;
        }

        .scroll-ruler-bar {
            height: 100%;
            width: 0%;
            background: var(--accent-text);
            transition: width 0.08s linear;
        }

        .brand {
            display: inline-flex;
            align-items: center;
            gap: 0.85rem;
            font-family: var(--font-mono);
            font-size: var(--step--1);
        }

        .brand__mark {
            width: 44px;
            height: 26px;
            color: var(--ink);
            transition: color var(--dur-1) var(--ease-out);
        }

        .brand__name {
            display: flex;
            align-items: baseline;
            gap: 0.35rem;
            color: var(--ink);
            font-weight: 500;
        }

        .brand__role {
            color: var(--muted);
            font-weight: 400;
        }

        .nav {
            justify-self: center;
        }

        .nav ul {
            display: flex;
            list-style: none;
            gap: 1.8rem;
            align-items: center;
        }

        .nav__link {
            display: inline-flex;
            align-items: baseline;
            gap: 0.4rem;
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            transition: color var(--dur-1) var(--ease-out);
            position: relative;
        }

        .nav__link:hover, .nav__link.is-active { color: var(--ink); }
        .nav__link .note { font-size: 0.72rem; color: var(--accent-text); }

        .header__actions {
            justify-self: end;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .telemetry-pill {
            font-family: var(--font-mono);
            font-size: 0.74rem;
            padding: 4px 10px;
            border: 1px solid var(--line);
            border-radius: 999px;
            background: var(--bg-raised);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--muted);
        }

        .telemetry-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--success);
            box-shadow: 0 0 8px var(--success);
            animation: pulseDot 2s infinite ease-in-out;
        }

        @keyframes pulseDot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.8); }
        }

        .header-btn {
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            padding: 5px 11px;
            border: 1px solid var(--line);
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all var(--dur-1) var(--ease-out);
        }

        .header-btn:hover {
            color: var(--ink);
            border-color: var(--line-strong);
            background: var(--bg-raised);
        }

        .kbd-tag {
            font-size: 0.68rem;
            background: var(--line);
            padding: 1px 5px;
            border-radius: 3px;
        }

        /* ===== HERO SECTION & DYNAMIC TERRAIN ===== */
        .hero {
            padding-top: calc(4.5rem + clamp(48px, 8vw, 110px));
            padding-bottom: clamp(60px, 9vw, 130px);
            display: flex;
            flex-direction: column;
            gap: clamp(32px, 5vw, 64px);
            min-height: 94vh;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
        }

        /* Dynamic Interactive Canvas Terrain (Topographic Contours) */
        #heroTerrainCanvas {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            opacity: 0.88;
            transition: opacity 0.5s ease;
        }

        /* ===== HERO CROSSHAIR AXIS HUD (PIERGORELLI SIGNATURE) ===== */
        .hero-crosshair {
            position: absolute;
            inset: 0;
            pointer-events: none;
            z-index: 4;
            opacity: 0;
            transition: opacity 0.2s ease;
            overflow: hidden;
        }

        .hero-crosshair.is-active {
            opacity: 1;
        }

        body.in-hero-crosshair .tech-cursor,
        body.in-hero-crosshair .tech-cursor-follower {
            opacity: 0 !important;
        }

        /* Horizontal Full-width Axis Line */
        .crosshair-axis-x {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: rgba(255, 255, 255, 0.22);
            pointer-events: none;
            will-change: transform;
        }

        [data-theme="light"] .crosshair-axis-x {
            background: rgba(14, 14, 13, 0.2);
        }

        /* Vertical Full-height Axis Line */
        .crosshair-axis-y {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            width: 1px;
            background: rgba(255, 255, 255, 0.22);
            pointer-events: none;
            will-change: transform;
        }

        [data-theme="light"] .crosshair-axis-y {
            background: rgba(14, 14, 13, 0.2);
        }

        /* Center Blue Square Reticle Target */
        .crosshair-target {
            position: absolute;
            top: 0;
            left: 0;
            width: 12px;
            height: 12px;
            background: #508aff;
            border: 1px solid rgba(255, 255, 255, 0.85);
            border-radius: 2px;
            pointer-events: none;
            box-shadow: 0 0 14px rgba(80, 138, 255, 0.6);
            will-change: transform;
        }

        [data-theme="light"] .crosshair-target {
            background: #2f5bff;
            border-color: rgba(255, 255, 255, 0.95);
        }

        /* Coordinates Label: X 1228 · Y 0340 */
        .crosshair-label {
            position: absolute;
            top: 0;
            left: 0;
            font-family: var(--font-mono);
            font-size: 0.82rem;
            font-weight: 500;
            letter-spacing: 0.05em;
            color: #ffffff;
            pointer-events: none;
            user-select: none;
            white-space: nowrap;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9), 0 0 8px rgba(0, 0, 0, 0.6);
            will-change: transform;
        }

        [data-theme="light"] .crosshair-label {
            color: #0e0e0d;
            text-shadow: 0 1px 4px rgba(255, 255, 255, 0.9);
        }

        .hero > *:not(#heroTerrainCanvas) {
            position: relative;
            z-index: 2;
        }

        .hero__top {
            border-top: 1px solid var(--line-strong);
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            gap: 1rem;
            padding-top: 0.85rem;
            flex-wrap: wrap;
        }

        .hero__title {
            display: flex;
            flex-direction: column;
            gap: clamp(16px, 2.5vw, 32px);
        }

        .hero__human {
            display: block;
            margin-left: -0.05em;
            color: var(--ink);
        }

        .hero__machine {
            max-width: 34ch;
            color: var(--muted);
            font-weight: 400;
            line-height: 1.25;
            min-height: 3.8em;
            transition: color var(--dur-1) var(--ease-out);
        }

        .hero__machine .highlight {
            color: var(--ink);
        }

        .hero__notes {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem 2.5rem;
            align-items: center;
        }

        .hero__notes .note {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .stream-btn {
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--accent-text);
            text-decoration: underline;
            text-underline-offset: 3px;
            cursor: pointer;
            transition: opacity var(--dur-1);
        }

        .stream-btn:hover { opacity: 0.75; }

        .hero__foot {
            border-top: 1px solid var(--line);
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            gap: 2rem;
            padding-top: 1.75rem;
            flex-wrap: wrap;
        }

        .hero__intro { max-width: 48ch; }
        .hero__ctas { display: flex; gap: 1rem; flex-wrap: wrap; }

        /* ===== [01] MANIFESTO & INTERACTIVE SCRUBBING ===== */
        .manifesto {
            padding-block: var(--section-gap);
        }

        .wf-row {
            position: relative;
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 1px dashed var(--line);
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
            overflow: hidden;
            cursor: crosshair;
        }

        .wf-line {
            width: fit-content;
            max-width: 100%;
            position: relative;
        }

        .wf-solid-reveal {
            position: absolute;
            inset: 0;
            color: var(--ink);
            clip-path: inset(0 100% 0 0);
            pointer-events: none;
            transition: clip-path 0.15s ease-out;
        }

        .wf-row:hover .wf-solid-reveal {
            clip-path: inset(0 0% 0 0);
        }

        .wf-dim {
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
        }

        .manifesto__body {
            margin-top: clamp(40px, 6vw, 80px);
        }

        .manifesto__body p { grid-column: 1 / span 9; }

        /* ===== [02] WORK STAGE ARCHITECTURAL SLIDER ===== */
        .work-section {
            padding-block: var(--section-gap);
        }

        .work__intro {
            max-width: 58ch;
            margin-bottom: clamp(36px, 5vw, 64px);
        }

        .ws-container {
            border: 1px solid var(--line);
            border-radius: 6px;
            background: var(--bg-raised);
            overflow: hidden;
            margin-bottom: clamp(40px, 6vw, 80px);
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.05);
        }

        .ws-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem var(--gutter);
            border-bottom: 1px solid var(--line);
            background: var(--bg);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .ws-project-selector {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }

        .ws-tab-btn {
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            padding: 5px 14px;
            border: 1px solid var(--line);
            border-radius: 4px;
            transition: all var(--dur-1) var(--ease-out);
        }

        .ws-tab-btn:hover { color: var(--ink); border-color: var(--line-strong); }

        .ws-tab-btn.is-active {
            color: var(--accent-text);
            border-color: var(--accent);
            background: var(--accent-dim);
            font-weight: 500;
        }

        .ws-stages-nav {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-mono);
            font-size: var(--step--1);
        }

        .stage-pill {
            padding: 5px 12px;
            border-radius: 4px;
            color: var(--muted);
            border: 1px solid transparent;
            cursor: pointer;
            transition: all var(--dur-1);
        }

        .stage-pill.is-active {
            color: var(--ink);
            background: var(--bg-raised);
            border-color: var(--line-strong);
            font-weight: 500;
        }

        .ws-body {
            display: grid;
            grid-template-columns: 1fr 1fr;
            min-height: 480px;
        }

        .ws-info-panel {
            padding: clamp(24px, 4vw, 48px);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-right: 1px solid var(--line);
        }

        .ws-interactive-canvas {
            padding: clamp(24px, 4vw, 48px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: var(--bg);
            position: relative;
            overflow: hidden;
        }

        /* Stage 1: Plot View */
        .stage-view {
            width: 100%;
            height: 100%;
            display: none;
            flex-direction: column;
            justify-content: center;
        }

        .stage-view.is-visible { display: flex; }

        .wireframe-blueprint-box {
            border: 1px dashed var(--line-strong);
            padding: 24px;
            position: relative;
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            line-height: 1.8;
            background: var(--bg-raised);
            border-radius: 4px;
        }

        .wireframe-blueprint-box::before {
            content: "ARCHITECTURAL BLUEPRINT // SPECIFICATION";
            position: absolute;
            top: -10px;
            left: 14px;
            background: var(--bg);
            padding: 0 8px;
            color: var(--accent-text);
            font-size: 0.68rem;
        }

        /* Stage 2: Build View */
        .code-matrix-box {
            background: var(--bg-surface);
            border: 1px solid var(--line);
            padding: 22px;
            font-family: var(--font-mono);
            font-size: 0.8rem;
            line-height: 1.8;
            color: var(--muted);
            border-radius: 4px;
            overflow-x: auto;
            width: 100%;
        }

        .code-matrix-box .key { color: var(--accent-text); }
        .code-matrix-box .str { color: var(--ink); }

        /* Stage 3: Live Interactive Demos */
        .live-interactive-panel {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }

        /* L&T Network Packet Simulator */
        .packet-sim {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 24px 16px;
            border: 1px solid var(--line);
            background: var(--bg-surface);
            border-radius: 4px;
            position: relative;
        }

        .sim-node {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            font-family: var(--font-mono);
            font-size: 0.72rem;
            z-index: 2;
        }

        .node-icon {
            width: 44px;
            height: 44px;
            border: 1px solid var(--line-strong);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--bg-raised);
            color: var(--ink);
            transition: all 0.3s ease;
        }

        .sim-wire {
            position: absolute;
            top: 41px;
            left: 56px;
            right: 56px;
            height: 2px;
            background: var(--line);
            z-index: 1;
        }

        .packet-dot {
            position: absolute;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent);
            box-shadow: 0 0 10px var(--accent);
            top: -5px;
            left: 0%;
            transition: left 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        /* OpenCV Interactive Sketch Canvas Component */
        .sketch-interactive-box {
            width: 100%;
            border: 1px solid var(--line);
            border-radius: 4px;
            background: var(--bg-surface);
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .sketch-canvas-wrap {
            position: relative;
            width: 100%;
            height: 180px;
            border: 1px solid var(--line);
            border-radius: 4px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #000;
        }

        #opencvCanvas {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .opencv-controls {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .filter-btn {
            font-family: var(--font-mono);
            font-size: 0.72rem;
            padding: 4px 10px;
            border: 1px solid var(--line);
            border-radius: 4px;
            background: var(--bg-raised);
            color: var(--muted);
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .filter-btn.is-active, .filter-btn:hover {
            color: var(--ink);
            border-color: var(--accent);
            background: var(--accent-dim);
        }

        /* Voice Waveform Component */
        .voice-interactive-box {
            width: 100%;
            border: 1px solid var(--line);
            border-radius: 4px;
            background: var(--bg-surface);
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .voice-canvas-wrap {
            height: 90px;
            width: 100%;
            border: 1px solid var(--line);
            border-radius: 4px;
            background: var(--bg-raised);
            overflow: hidden;
        }

        #voiceCanvas {
            width: 100%;
            height: 100%;
        }

        .voice-log-text {
            font-family: var(--font-mono);
            font-size: 0.76rem;
            color: var(--muted);
            min-height: 2.4em;
            line-height: 1.5;
        }

        /* Tag Pill */
        .work-tech-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1.5rem;
        }

        .work-tag {
            font-family: var(--font-mono);
            font-size: 0.74rem;
            padding: 3px 10px;
            border: 1px solid var(--line);
            border-radius: 999px;
            color: var(--muted);
            background: var(--bg);
        }

        /* ===== [03] CAPABILITIES & INTERACTIVE REST PLAYGROUND ===== */
        .capabilities-section {
            padding-block: var(--section-gap);
        }

        .rest-client-box {
            border: 1px solid var(--line);
            border-radius: 6px;
            background: var(--bg-raised);
            margin-top: 2.5rem;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        }

        .rest-client-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 18px;
            background: var(--bg);
            border-bottom: 1px solid var(--line);
            font-family: var(--font-mono);
            font-size: var(--step--1);
        }

        .rest-request-bar {
            display: flex;
            padding: 14px 18px;
            gap: 10px;
            border-bottom: 1px solid var(--line);
            background: var(--bg-surface);
            align-items: center;
            flex-wrap: wrap;
        }

        .http-method {
            font-family: var(--font-mono);
            font-weight: 700;
            font-size: 0.8rem;
            padding: 6px 12px;
            border-radius: 4px;
            background: var(--accent-dim);
            color: var(--accent-text);
        }

        .endpoint-select {
            flex: 1;
            min-width: 260px;
            font-family: var(--font-mono);
            font-size: 0.85rem;
            padding: 7px 12px;
            border: 1px solid var(--line);
            border-radius: 4px;
            background: var(--bg);
            color: var(--ink);
            outline: none;
        }

        .send-req-btn {
            font-family: var(--font-mono);
            font-size: 0.8rem;
            padding: 7px 18px;
            border-radius: 4px;
            background: var(--ink);
            color: var(--bg);
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .send-req-btn:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }

        .rest-response-area {
            display: grid;
            grid-template-columns: 240px 1fr;
            min-height: 240px;
        }

        .rest-meta-pane {
            border-right: 1px solid var(--line);
            padding: 16px;
            font-family: var(--font-mono);
            font-size: 0.74rem;
            display: flex;
            flex-direction: column;
            gap: 12px;
            background: var(--bg-raised);
        }

        .meta-stat-item {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .meta-stat-label { color: var(--muted); }
        .meta-stat-val { color: var(--ink); font-weight: 600; }

        .rest-json-pane {
            padding: 16px 20px;
            font-family: var(--font-mono);
            font-size: 0.8rem;
            line-height: 1.7;
            overflow-x: auto;
            background: var(--bg-surface);
            color: var(--muted);
            position: relative;
        }

        .copy-json-btn {
            position: absolute;
            top: 12px;
            right: 16px;
            font-family: var(--font-mono);
            font-size: 0.72rem;
            padding: 3px 8px;
            border: 1px solid var(--line);
            border-radius: 3px;
            background: var(--bg-raised);
            color: var(--muted);
            cursor: pointer;
        }

        .copy-json-btn:hover { color: var(--ink); border-color: var(--ink); }

        /* Syntax colors */
        .json-key { color: var(--accent-text); }
        .json-str { color: var(--success); }
        .json-num { color: #f59e0b; }
        .json-bool { color: #ec4899; }

        /* Code Inspector Section */
        .code-inspector-container {
            border: 1px solid var(--line);
            border-radius: 6px;
            background: var(--bg-raised);
            margin-top: 2rem;
            overflow: hidden;
        }

        .code-tabs {
            display: flex;
            border-bottom: 1px solid var(--line);
            background: var(--bg);
            overflow-x: auto;
        }

        .code-tab-btn {
            padding: 0.85rem 1.4rem;
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
            border-right: 1px solid var(--line);
            white-space: nowrap;
            transition: all var(--dur-1);
        }

        .code-tab-btn:hover { color: var(--ink); background: var(--bg-raised); }

        .code-tab-btn.is-active {
            color: var(--ink);
            background: var(--bg-raised);
            font-weight: 500;
            border-bottom: 2px solid var(--accent);
        }

        .code-editor-content {
            padding: 24px;
            font-family: var(--font-mono);
            font-size: 0.84rem;
            line-height: 1.75;
            background: var(--bg-surface);
            overflow-x: auto;
        }

        .code-editor-content pre { margin: 0; }
        .code-editor-content .kw { color: var(--accent-text); font-weight: 600; }
        .code-editor-content .fn { color: #10b981; }
        .code-editor-content .st { color: #f59e0b; }
        .code-editor-content .cm { color: var(--muted); font-style: italic; }

        /* ===== [04] BACKGROUND & CREDENTIALS ===== */
        .education-section {
            padding-block: var(--section-gap);
        }

        .edu-split {
            display: grid;
            grid-template-columns: 7fr 5fr;
            gap: clamp(24px, 4vw, 56px);
            margin-top: 2rem;
        }

        .degree-box {
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: clamp(24px, 4vw, 40px);
            background: var(--bg-raised);
            position: relative;
        }

        .edu-aside {
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: clamp(24px, 4vw, 36px);
            background: var(--bg-surface);
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .cert-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            padding-bottom: 0.75rem;
            margin-bottom: 0.75rem;
            border-bottom: 1px dashed var(--line);
            font-size: var(--step--1);
        }

        .cert-row:last-child { border-bottom: none; }

        /* ===== [05] BEYOND CODE ===== */
        .interests-section {
            padding-block: var(--section-gap);
        }

        .interests-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .interest-item {
            border: 1px solid var(--line);
            border-radius: 6px;
            padding: 24px;
            background: var(--bg-raised);
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            transition: transform var(--dur-1) var(--ease-out), border-color var(--dur-1);
        }

        .interest-item:hover {
            transform: translateY(-3px);
            border-color: var(--line-strong);
        }

        .interest-item h3 { font-size: var(--step-0); font-weight: 500; color: var(--ink); }
        .interest-item p { font-size: var(--step--1); color: var(--muted); line-height: 1.6; }

        /* ===== [06] NEXT / CONTACT ===== */
        .cta-section {
            padding-block: var(--section-gap);
        }

        .cta-title {
            margin-bottom: clamp(32px, 5vw, 64px);
        }

        .cta-channels {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            border-top: 1px solid var(--line);
            border-bottom: 1px solid var(--line);
        }

        .cta-item {
            padding: clamp(24px, 4vw, 48px);
            border-right: 1px solid var(--line);
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            transition: background var(--dur-1);
        }

        .cta-item:last-child { border-right: none; }
        .cta-item:hover { background: var(--bg-raised); }

        .cta-value {
            font-size: var(--step-1);
            color: var(--ink);
            font-weight: 500;
            display: inline-flex;
            align-items: baseline;
            gap: 0.25rem;
        }

        /* ===== SITE FOOTER ===== */
        .site-footer {
            border-top: 1px solid var(--line-strong);
            padding-block: 2.5rem;
            font-family: var(--font-mono);
            font-size: var(--step--1);
            color: var(--muted);
        }

        .footer-wrap {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }

        /* ===== DOCKED INTERACTIVE DEVELOPER TERMINAL (REPL) ===== */
        .dev-terminal-dock {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: clamp(320px, 32vw, 460px);
            background: var(--bg-surface);
            border: 1px solid var(--line-strong);
            border-radius: 8px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.28);
            z-index: 900;
            font-family: var(--font-mono);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.3s ease;
        }

        .dev-terminal-dock.is-minimized {
            transform: translateY(calc(100% - 38px));
        }

        .dev-terminal-dock.is-hidden {
            opacity: 0;
            pointer-events: none;
            transform: translateY(20px);
        }

        .terminal-titlebar {
            height: 38px;
            background: var(--bg-raised);
            border-bottom: 1px solid var(--line);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-inline: 12px;
            cursor: pointer;
            user-select: none;
        }

        .terminal-titlebar-left {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.74rem;
            color: var(--muted);
        }

        .terminal-actions {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .terminal-btn-icon {
            font-size: 0.72rem;
            color: var(--muted);
            padding: 3px 6px;
            border-radius: 3px;
        }

        .terminal-btn-icon:hover { color: var(--ink); background: var(--bg); }

        .terminal-body {
            padding: 12px 14px;
            height: 220px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 8px;
            font-size: 0.76rem;
            line-height: 1.5;
            background: var(--bg-surface);
        }

        .terminal-chips {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
            padding-bottom: 6px;
            border-bottom: 1px dashed var(--line);
        }

        .chip-btn {
            font-family: var(--font-mono);
            font-size: 0.68rem;
            padding: 2px 7px;
            border: 1px solid var(--line);
            border-radius: 3px;
            background: var(--bg-raised);
            color: var(--accent-text);
            cursor: pointer;
        }

        .chip-btn:hover { background: var(--accent-dim); }

        .terminal-output {
            color: var(--muted);
            white-space: pre-wrap;
        }

        .terminal-input-row {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 12px;
            border-top: 1px solid var(--line);
            background: var(--bg-raised);
        }

        .terminal-prompt {
            color: var(--accent-text);
            font-weight: 600;
            font-size: 0.75rem;
        }

        .terminal-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: var(--ink);
            font-family: var(--font-mono);
            font-size: 0.76rem;
        }

        /* Toggle Terminal Floating Trigger Pill */
        .terminal-floating-pill {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 899;
            font-family: var(--font-mono);
            font-size: 0.75rem;
            padding: 8px 14px;
            border: 1px solid var(--line-strong);
            background: var(--bg-raised);
            border-radius: 999px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
            display: none;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .terminal-floating-pill:hover {
            border-color: var(--ink);
            transform: translateY(-2px);
        }

        /* ===== COMMAND PALETTE OVERLAY (⌘K) ===== */
        .cmd-backdrop {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(8px);
            z-index: 10000;
            display: none;
            align-items: flex-start;
            justify-content: center;
            padding-top: 15vh;
        }

        .cmd-backdrop.is-open { display: flex; }

        .cmd-panel {
            width: min(620px, 92vw);
            background: var(--bg-raised);
            border: 1px solid var(--line-strong);
            border-radius: 8px;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
            overflow: hidden;
            font-family: var(--font-mono);
            animation: cmdPop 0.18s var(--ease-out);
        }

        @keyframes cmdPop {
            from { opacity: 0; transform: scale(0.97) translateY(-8px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .cmd-input-bar {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px 18px;
            border-bottom: 1px solid var(--line);
            background: var(--bg);
        }

        .cmd-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            font-family: var(--font-mono);
            font-size: var(--step-0);
            color: var(--ink);
        }

        .cmd-list {
            max-height: 340px;
            overflow-y: auto;
            padding: 8px;
        }

        .cmd-option {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 14px;
            border-radius: 4px;
            color: var(--muted);
            cursor: pointer;
            font-size: var(--step--1);
            transition: background 0.15s, color 0.15s;
        }

        .cmd-option:hover, .cmd-option.is-selected {
            background: var(--bg-surface);
            color: var(--ink);
        }

        /* Responsive Breakpoints */
        @media (max-width: 900px) {
            .site-header { grid-template-columns: 1fr auto; }
            .nav { display: none; }
            .ws-body { grid-template-columns: 1fr; }
            .ws-info-panel { border-right: none; border-bottom: 1px solid var(--line); }
            .edu-split { grid-template-columns: 1fr; }
            .interests-grid { grid-template-columns: repeat(2, 1fr); }
            .cta-channels { grid-template-columns: 1fr; }
            .cta-item { border-right: none; border-bottom: 1px solid var(--line); }
            .rest-response-area { grid-template-columns: 1fr; }
            .rest-meta-pane { border-right: none; border-bottom: 1px solid var(--line); }
            .dev-terminal-dock { width: calc(100vw - 32px); right: 16px; bottom: 16px; }
        }
    </style>
</head>
<body>

    <!-- ===== 1. COMPILE INTRO PRELOADER (ARCHITECTURAL BOOT) ===== -->
    <div class="preloader" id="compilePreloader" aria-hidden="true">
        <div class="preloader__meta">
            <span>boot://shubhankar.dev · kernel.init</span>
            <span class="note--accent">REV. 2026.3 // PROD_RELEASE</span>
            <button class="preloader__skip-btn" id="skipPreloaderBtn">Skip [ESC]</button>
        </div>

        <div class="preloader__center">
            <!-- Animated Monogram -->
            <svg class="preloader__mark" viewBox="0 0 68 40" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M 22 10 C 12 10 8 16 14 21 C 22 26 22 32 10 32"></path>
                <path d="M 38 32 V 10 L 56 32 V 10"></path>
                <circle cx="62" cy="32" r="2.2" fill="currentColor"></circle>
            </svg>

            <!-- Real-time kernel boot log stream -->
            <div class="preloader__console" id="preloaderConsole">
                <div class="preloader__log-line active"><span class="tag">[0.05s]</span><span>KERNEL: Initializing Shubhankar Negi runtime engine...</span></div>
                <div class="preloader__log-line" id="log2"><span class="tag">[0.35s]</span><span>AUTH: Larsen &amp; Toubro enterprise node connected (Pune)...</span></div>
                <div class="preloader__log-line" id="log3"><span class="tag">[0.75s]</span><span>STACK: JVM 21, Spring Boot, MySQL pool &amp; OpenCV 4.x mounted.</span></div>
                <div class="preloader__log-line" id="log4"><span class="tag">[1.20s]</span><span>SHADERS: Himalayan contour canvas &amp; REPL terminal ready.</span></div>
                <div class="preloader__log-line" id="log5"><span class="tag">[1.50s]</span><span>SYSTEM: All subsystems nominal. Hydrating DOM.</span></div>
            </div>

            <!-- Precision Progress Bar -->
            <div class="preloader__progress-bar-wrap">
                <div class="preloader__progress-bar" id="preloaderProgressBar"></div>
            </div>
        </div>

        <div class="preloader__foot">
            <span>Full Stack Developer @ L&amp;T · Pune &amp; Almora</span>
            <span class="preloader__count" id="preloaderPercent">00%</span>
        </div>
    </div>

    <!-- Blueprint Grid Mode Overlay -->
    <div class="blueprint-grid-overlay" aria-hidden="true"></div>
    <div class="hud-dimensions" id="hudDim">VIEWPORT: 1440 × 900 · GRID 32px · NODE: ALMORA/PUNE</div>

    <!-- Matrix Code Rain Canvas -->
    <canvas id="matrixCanvas"></canvas>
    <button class="matrix-exit-btn" id="exitMatrixBtn">EXIT MATRIX [ESC]</button>

    <!-- Precision Crosshair Cursor -->
    <div class="tech-cursor" id="techCursor" aria-hidden="true"></div>
    <div class="tech-cursor-follower" id="techCursorFollower" aria-hidden="true"></div>

    <!-- ===== SITE HEADER ===== -->
    <header class="site-header wrap">
        <a href="#hero" class="brand" aria-label="Shubhankar Negi, home">
            <!-- Geometric Monogram SVG -->
            <svg class="brand__mark" viewBox="0 0 68 40" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M 22 10 C 12 10 8 16 14 21 C 22 26 22 32 10 32"></path>
                <path d="M 38 32 V 10 L 56 32 V 10"></path>
                <circle cx="62" cy="32" r="2.2" fill="currentColor"></circle>
            </svg>
            <span class="brand__name">
                <span data-scramble>Shubhankar Negi</span>
                <span class="brand__role">/ full stack</span>
            </span>
        </a>

        <nav class="nav" aria-label="Main Navigation">
            <ul>
                <li><a href="#work" class="nav__link"><span class="note">01</span><span data-scramble>Work</span></a></li>
                <li><a href="#philosophy" class="nav__link"><span class="note">02</span><span data-scramble>Philosophy</span></a></li>
                <li><a href="#capabilities" class="nav__link"><span class="note">03</span><span data-scramble>API &amp; Stack</span></a></li>
                <li><a href="#background" class="nav__link"><span class="note">04</span><span data-scramble>Background</span></a></li>
                <li><a href="#contact" class="nav__link"><span class="note">05</span><span data-scramble>Contact</span></a></li>
            </ul>
        </nav>

        <div class="header__actions">
            <!-- Live L&T Telemetry Pill -->
            <div class="telemetry-pill" title="Current live employment node">
                <span class="telemetry-dot"></span>
                <span>L&amp;T PUNE</span>
                <span class="note--accent" id="headerClock">12:00 IST</span>
            </div>

            <!-- Sound Synthesis Toggle -->
            <button class="header-btn" id="soundToggleBtn" title="Toggle Haptic Sound Synthesis">
                <i class="fa-solid fa-volume-xmark" id="soundIcon"></i>
                <span id="soundLabel">SFX</span>
            </button>

            <!-- Theme Toggle -->
            <button class="header-btn" id="themeToggleBtn" title="Toggle Light/Dark Theme">
                <i class="fa-solid fa-circle-half-stroke"></i>
                <span id="themeLabel">THEME</span>
            </button>

            <!-- Blueprint Grid Toggle -->
            <button class="header-btn" id="gridToggleBtn" title="Toggle Blueprint Grid Mode [G]">
                <span>GRID</span>
                <span class="kbd-tag">G</span>
            </button>

            <!-- Command Palette Toggle -->
            <button class="header-btn" id="cmdToggleBtn" title="Open Quick Command Palette [⌘K]">
                <i class="fa-solid fa-terminal" style="font-size:0.75rem;"></i>
                <span class="kbd-tag">⌘K</span>
            </button>
        </div>

        <!-- Scroll Depth Calibrated Ruler -->
        <div class="scroll-ruler-track">
            <div class="scroll-ruler-bar" id="scrollRulerBar"></div>
        </div>
    </header>

    <!-- ===== MAIN CONTENT ===== -->
    <main>

        <!-- ================= HERO ================= -->
        <section class="hero wrap" id="hero">
            <!-- Dynamic Interactive Topographic Contour Canvas -->
            <canvas id="heroTerrainCanvas"></canvas>

            <!-- Crosshair Axis HUD Overlay -->
            <div class="hero-crosshair" id="heroCrosshair" aria-hidden="true">
                <div class="crosshair-axis-x" id="crosshairAxisX"></div>
                <div class="crosshair-axis-y" id="crosshairAxisY"></div>
                <div class="crosshair-target" id="crosshairTarget"></div>
                <div class="crosshair-label" id="crosshairLabel">X 0000 &middot; Y 0000</div>
            </div>

            <div class="hero__top note">
                <span data-scramble>Shubhankar Negi · Full Stack Developer</span>
                <span id="terrainCoords">Base camp · Pune &amp; Almora · 29.59° N, 79.65° E</span>
                <span class="note--success">● Active @ Larsen &amp; Toubro (L&amp;T)</span>
            </div>

            <div class="hero__title">
                <h1 class="hero__human display" data-scramble>I build software.</h1>
                <p class="hero__machine h2" id="streamTarget">
                    Full Stack Developer at <span class="highlight">Larsen &amp; Toubro</span>, turning complex requirements into resilient production code.
                </p>
            </div>

            <div class="hero__notes">
                <p class="note"><span class="note--accent">●</span> human · engineered with precision</p>
                <p class="note">
                    <span class="note--accent">◆</span> machine · 
                    <span id="tokenMetric">24</span> tokens · 
                    <span id="latencyMetric">140ms</span> · 
                    <button class="stream-btn" id="streamCycleBtn">↺ regenerate focus</button>
                </p>
                <p class="note" id="elevationDisplay"><span class="note--accent">▲</span> terrain · elevation 2,420m · hover to perturb</p>
            </div>

            <div class="hero__foot">
                <p class="hero__intro lead">
                    Bridging scalable backend microservices with high-performance responsive interfaces. From enterprise web applications at L&amp;T to real-time OpenCV computer vision matrices.
                </p>
                <div class="hero__ctas">
                    <a href="#contact" class="btn">Initiate contact <span class="arrow">→</span></a>
                    <a href="#work" class="btn btn--ghost">Explore selected work</a>
                    <a href="Shubhankar_Negi_Resume.pdf" download="Shubhankar_Negi_Resume.pdf" class="btn btn--ghost">
                        <i class="fa-solid fa-file-arrow-down" style="font-size:0.85rem;"></i> Resume (PDF)
                    </a>
                </div>
            </div>
        </section>

        <!-- ================= [01] PHILOSOPHY / MANIFESTO ================= -->
        <section class="manifesto wrap reveal-on-scroll" id="philosophy">
            <header class="section-head">
                <span class="note note--ink" data-scramble>[01] Philosophy</span>
                <span class="note">fig. 01 · wireframe → enterprise production</span>
            </header>

            <div class="wf-row" data-scrub>
                <p class="wf-line h1">
                    <span class="outline-text">Keep the logic.</span>
                    <span class="wf-solid-reveal">Keep the logic.</span>
                </p>
                <span class="wf-dim note">↤ 12 col ↦</span>
            </div>

            <div class="wf-row" data-scrub>
                <p class="wf-line h1">
                    <span class="outline-text">Solve what stands</span>
                    <span class="wf-solid-reveal">Solve what stands</span>
                </p>
                <span class="wf-dim note">font-size: var(--step-4)</span>
            </div>

            <div class="wf-row" data-scrub>
                <p class="wf-line h1">
                    <span class="outline-text">in its way.</span>
                    <span class="wf-solid-reveal">in its way.</span>
                </p>
                <span class="wf-dim note">ls −0.05em</span>
            </div>

            <div class="manifesto__body grid-12">
                <p class="lead">
                    Complex enterprise demands require clean engineering under the hood. Whether building multi-tier services at <strong>Larsen &amp; Toubro</strong>, optimizing MySQL relational schemas, or calculating OpenCV 21×21 Gaussian dodge matrices, I build systems that remain resilient, maintainable, and fast in production.
                </p>
            </div>
        </section>

        <!-- ================= [02] SELECTED WORK (3-STAGE ARCHITECTURAL FIELD REPORTS) ================= -->
        <section class="work-section wrap reveal-on-scroll" id="work">
            <header class="section-head">
                <span class="note note--ink" data-scramble>[02] Selected work</span>
                <span class="note">Interactive Field Reports · 3 Stages</span>
            </header>

            <p class="work__intro lead">
                Inspect how each engineering system was conceptualized, built, and deployed. Toggle between the three operational views: <strong>Plot (Wireframe)</strong>, <strong>Build (Code Structure)</strong>, and <strong>Live (Active Interactive Simulation)</strong>.
            </p>

            <!-- Signature Work Stage Component -->
            <div class="ws-container">
                <div class="ws-header">
                    <div class="ws-project-selector">
                        <button class="ws-tab-btn is-active" data-project="0">01 / L&amp;T Enterprise</button>
                        <button class="ws-tab-btn" data-project="1">02 / OpenCV Sketch CV</button>
                        <button class="ws-tab-btn" data-project="2">03 / Voice Assistant</button>
                        <button class="ws-tab-btn" data-project="3">04 / Feedback System</button>
                    </div>

                    <div class="ws-stages-nav">
                        <span class="note">STAGE:</span>
                        <button class="stage-pill is-active" data-stage="plot">01 Plot</button>
                        <button class="stage-pill" data-stage="build">02 Build</button>
                        <button class="stage-pill" data-stage="live">03 Live</button>
                    </div>
                </div>

                <div class="ws-body">
                    <!-- Left: Metadata & Narrative -->
                    <div class="ws-info-panel">
                        <div>
                            <div class="note note--accent" id="wsMetaDate" style="margin-bottom:0.75rem;">MAR 2026 — PRESENT · PUNE</div>
                            <h2 class="h2" id="wsProjectTitle" style="margin-bottom:1rem;" data-scramble>Enterprise Full-Stack Architecture</h2>
                            <p class="note" id="wsProjectDesc" style="font-size:var(--step-0); line-height:1.65; margin-bottom:1.5rem;">
                                Engineering scalable microservices, responsive web views, and high-throughput API endpoints at Larsen &amp; Toubro. Built for mission-critical reliability across multi-tenant enterprise workflows.
                            </p>
                        </div>
                        <div class="work-tech-tags" id="wsTechTags">
                            <span class="work-tag">Full Stack Development</span>
                            <span class="work-tag">Microservices</span>
                            <span class="work-tag">REST APIs</span>
                            <span class="work-tag">MySQL Cluster</span>
                        </div>
                    </div>

                    <!-- Right: Dynamic Stage Canvas -->
                    <div class="ws-interactive-canvas">
                        <!-- Stage 1: Plot View -->
                        <div class="stage-view is-visible" id="stagePlotView">
                            <div class="wireframe-blueprint-box">
                                <div id="plotDiagramText">
[BROWSER CLIENT: HTML5/JS]<br>
&nbsp;&nbsp;│ (HTTPS / JSON)<br>
&nbsp;&nbsp;▼<br>
[GATEWAY PROXY: TOMCAT/REVERSE-PROXY]<br>
&nbsp;&nbsp;│<br>
&nbsp;&nbsp;├──▶ [SERVICE CONTROLLER: JAVA / SPRING / SERVLETS]<br>
&nbsp;&nbsp;└──▶ [DATA REPOSITORY: MYSQL ACID PERSISTENCE]
                                </div>
                                <div style="margin-top:14px; font-size:0.7rem; color:var(--accent-text);">
                                    ↤ SPECS: LATENCY &lt; 25ms · TOLERANCE: 99.9% ↦
                                </div>
                            </div>
                        </div>

                        <!-- Stage 2: Build View -->
                        <div class="stage-view" id="stageBuildView">
                            <div class="code-matrix-box" id="buildCodeText">
<span class="key">struct</span> <span class="str">SystemDeployment</span> {<br>
&nbsp;&nbsp;organization: <span class="str">"Larsen &amp; Toubro (L&amp;T)"</span>,<br>
&nbsp;&nbsp;role: <span class="str">"Full Stack Developer"</span>,<br>
&nbsp;&nbsp;endpoints: <span class="str">"/api/v2/enterprise/telemetry"</span>,<br>
&nbsp;&nbsp;throughput: <span class="key">"10k req/min"</span>,<br>
&nbsp;&nbsp;persistence: <span class="str">"MySQL InnoDB + Indexed Keys"</span><br>
}
                            </div>
                        </div>

                        <!-- Stage 3: Live Interactive Simulation View -->
                        <div class="stage-view" id="stageLiveView">
                            <div class="live-interactive-panel" id="livePanelContent">
                                <!-- Dynamic Simulation Widget -->
                                <div class="packet-sim">
                                    <div class="sim-node">
                                        <div class="node-icon" id="nodeClient"><i class="fa-solid fa-desktop"></i></div>
                                        <span>CLIENT</span>
                                    </div>
                                    <div class="sim-wire">
                                        <div class="packet-dot" id="simPacketDot"></div>
                                    </div>
                                    <div class="sim-node">
                                        <div class="node-icon" id="nodeGateway"><i class="fa-solid fa-server"></i></div>
                                        <span>GATEWAY</span>
                                    </div>
                                    <div class="sim-node">
                                        <div class="node-icon" id="nodeDb"><i class="fa-solid fa-database"></i></div>
                                        <span>DATABASE</span>
                                    </div>
                                </div>
                                <div style="display:flex; justify-content:space-between; align-items:center;">
                                    <span class="note" id="simStatusMsg">STATUS: IDLE · READY FOR PAYLOAD</span>
                                    <button class="btn btn--ghost" id="fireSimBtn" style="height:2.4rem; padding-inline:1rem; font-size:0.8rem;">
                                        Dispatch Request <i class="fa-solid fa-bolt" style="font-size:0.7rem; margin-left:4px;"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ================= [03] CAPABILITIES & INTERACTIVE REST PLAYGROUND ================= -->
        <section class="capabilities-section wrap reveal-on-scroll" id="capabilities">
            <header class="section-head">
                <span class="note note--ink" data-scramble>[03] Capabilities</span>
                <span class="note">Interactive REST Client &amp; Source Inspector</span>
            </header>

            <p class="lead" style="max-width:58ch;">
                Full-stack development demands rigorous verification. Test Shubhankar's live API endpoints below, or inspect implementation code patterns from his core stack:
            </p>

            <!-- Interactive REST Client / Playground -->
            <div class="rest-client-box">
                <div class="rest-client-header">
                    <span class="note--accent">REST_BENCHMARK_PROBE // v1.2</span>
                    <span class="note">SSL / TLS 1.3 · HTTP/2</span>
                </div>
                <div class="rest-request-bar">
                    <span class="http-method">GET</span>
                    <select class="endpoint-select" id="restEndpointSelect">
                        <option value="lnt">/api/v1/employment/larsen-toubro</option>
                        <option value="profile">/api/v1/developer/profile</option>
                        <option value="cv">/api/v1/projects/opencv-sketch</option>
                        <option value="feedback">/api/v1/projects/student-feedback</option>
                    </select>
                    <button class="send-req-btn" id="restSendBtn">
                        <i class="fa-solid fa-paper-plane"></i> Send HTTP Request
                    </button>
                </div>
                <div class="rest-response-area">
                    <div class="rest-meta-pane">
                        <div class="meta-stat-item">
                            <span class="meta-stat-label">STATUS</span>
                            <span class="meta-stat-val note--success" id="restStatusVal">200 OK</span>
                        </div>
                        <div class="meta-stat-item">
                            <span class="meta-stat-label">ROUNDTRIP TIME</span>
                            <span class="meta-stat-val" id="restLatencyVal">14 ms</span>
                        </div>
                        <div class="meta-stat-item">
                            <span class="meta-stat-label">PAYLOAD SIZE</span>
                            <span class="meta-stat-val" id="restSizeVal">482 B</span>
                        </div>
                        <div class="meta-stat-item">
                            <span class="meta-stat-label">SERVER NODE</span>
                            <span class="meta-stat-val">L&amp;T Pune [18.52° N]</span>
                        </div>
                    </div>
                    <div class="rest-json-pane">
                        <button class="copy-json-btn" id="copyJsonBtn">Copy JSON</button>
                        <pre><code id="restJsonDisplay">{
  <span class="json-key">"organization"</span>: <span class="json-str">"Larsen &amp; Toubro (L&amp;T)"</span>,
  <span class="json-key">"role"</span>: <span class="json-str">"Full Stack Developer"</span>,
  <span class="json-key">"location"</span>: <span class="json-str">"Pune, Maharashtra"</span>,
  <span class="json-key">"status"</span>: <span class="json-str">"Active (March 2026 — Present)"</span>,
  <span class="json-key">"stack"</span>: [<span class="json-str">"Java"</span>, <span class="json-str">"Spring Boot"</span>, <span class="json-str">"MySQL"</span>, <span class="json-str">"Microservices"</span>],
  <span class="json-key">"uptime"</span>: <span class="json-num">99.98</span>,
  <span class="json-key">"verified"</span>: <span class="json-bool">true</span>
}</code></pre>
                    </div>
                </div>
            </div>

            <!-- Tabbed Code Inspector -->
            <div class="code-inspector-container">
                <div class="code-tabs">
                    <button class="code-tab-btn is-active" data-lang="java">01 // Java Enterprise Servlet</button>
                    <button class="code-tab-btn" data-lang="python">02 // Python OpenCV Pipeline</button>
                    <button class="code-tab-btn" data-lang="sql">03 // SQL Schema &amp; Relations</button>
                    <button class="code-tab-btn" data-lang="devops">04 // Production Linux Shell</button>
                </div>
                <div class="code-editor-content">
                    <pre><code id="codeDisplayArea"><span class="cm">// Java Enterprise Servlet Controller</span>
<span class="kw">public class</span> FeedbackController <span class="kw">extends</span> HttpServlet {
    <span class="kw">private</span> FeedbackDAO feedbackDao = <span class="kw">new</span> FeedbackDAO();

    <span class="kw">protected void</span> doPost(HttpServletRequest req, HttpServletResponse resp) {
        String studentId = req.getParameter(<span class="st">"student_id"</span>);
        <span class="kw">int</span> instructorScore = Integer.parseInt(req.getParameter(<span class="st">"score"</span>));
        
        <span class="cm">// Validate payload &amp; compute aggregate statistics</span>
        feedbackDao.recordMetric(studentId, instructorScore);
        resp.setStatus(HttpServletResponse.SC_OK);
    }
}</code></pre>
                </div>
            </div>
        </section>

        <!-- ================= [04] BACKGROUND & CREDENTIALS ================= -->
        <section class="education-section wrap reveal-on-scroll" id="background">
            <header class="section-head">
                <span class="note note--ink" data-scramble>[04] Education &amp; Credentials</span>
                <span class="note">Academic foundation &amp; accreditations</span>
            </header>

            <div class="edu-split">
                <div class="edu-main">
                    <div class="degree-box">
                        <span class="note note--accent">AUG 2022 — MAY 2025</span>
                        <h2 class="h2" style="margin-top:0.5rem; margin-bottom:0.25rem;" data-scramble>Bachelor of Technology in Computer Science</h2>
                        <p class="note" style="margin-bottom:1.5rem;">Graphic Era Hill University · Bhimtal Campus, Uttarakhand</p>

                        <p class="lead" style="font-size:var(--step-0); margin-bottom:1.5rem;">
                            Rigorous university curriculum grounded in core computing fundamentals:
                        </p>

                        <div class="work-tech-tags">
                            <span class="work-tag">Data Structures &amp; Algorithms</span>
                            <span class="work-tag">Database Management Systems</span>
                            <span class="work-tag">Artificial Intelligence</span>
                            <span class="work-tag">Computer Architecture</span>
                            <span class="work-tag">Software Development</span>
                            <span class="work-tag">Cyber Security</span>
                            <span class="work-tag">Cryptography</span>
                        </div>
                    </div>
                </div>

                <div class="edu-aside">
                    <span class="note note--ink" data-scramble>Verified Certifications</span>
                    <div>
                        <div class="cert-row">
                            <span>Project Development Using Java</span>
                            <span class="note note--accent">Udemy · Complete</span>
                        </div>
                        <div class="cert-row">
                            <span>Python Programming Complete Bootcamp</span>
                            <span class="note note--accent">Udemy · Complete</span>
                        </div>
                        <div class="cert-row">
                            <span>Linux for Absolute Beginners</span>
                            <span class="note note--accent">Udemy · Complete</span>
                        </div>
                    </div>

                    <span class="note note--ink" style="margin-top:0.5rem;" data-scramble>Professional Strengths</span>
                    <p class="note" style="line-height:1.7;">
                        Rapid learning curve · High technical ownership · Analytical root-cause problem solver · Disciplined and sincere · Cross-functional collaborator.
                    </p>
                </div>
            </div>
        </section>

        <!-- ================= [05] BEYOND CODE ================= -->
        <section class="interests-section wrap reveal-on-scroll" id="interests">
            <header class="section-head">
                <span class="note note--ink" data-scramble>[05] Beyond Code</span>
                <span class="note">Human perspective</span>
            </header>

            <div class="interests-grid">
                <div class="interest-item">
                    <span class="note note--accent">01</span>
                    <h3 data-scramble>Technology</h3>
                    <p>Continuously exploring full-stack patterns, container orchestration, and high-performance computing frameworks.</p>
                </div>
                <div class="interest-item">
                    <span class="note note--accent">02</span>
                    <h3 data-scramble>Travel</h3>
                    <p>Visiting historical landmarks of geographic, architectural, and cultural heritage across India.</p>
                </div>
                <div class="interest-item">
                    <span class="note note--accent">03</span>
                    <h3 data-scramble>Trekking</h3>
                    <p>Himalayan high-altitude trail trekking to build endurance, mental clarity, and adaptive problem solving.</p>
                </div>
                <div class="interest-item">
                    <span class="note note--accent">04</span>
                    <h3 data-scramble>Gaming</h3>
                    <p>Strategic virtual worlds that test spatial reasoning, tactical reflexes, and synchronized team cooperation.</p>
                </div>
            </div>
        </section>

        <!-- ================= [06] NEXT / CONTACT ================= -->
        <section class="cta-section wrap reveal-on-scroll" id="contact">
            <header class="section-head">
                <span class="note note--ink" data-scramble>[06] Next</span>
                <span class="note">Direct communication channels</span>
            </header>

            <h2 class="display cta-title" data-scramble>Tell me what you're building.</h2>

            <div class="cta-channels">
                <div class="cta-item">
                    <span class="note">Direct Email</span>
                    <a href="mailto:samnegi1844@gmail.com" class="cta-value">samnegi1844@gmail.com ↗</a>
                    <span class="note">Fast response time</span>
                </div>

                <div class="cta-item">
                    <span class="note">Telephone / WhatsApp</span>
                    <a href="tel:+918650051616" class="cta-value">+91 86500 51616 ↗</a>
                    <span class="note">Voice &amp; WhatsApp communication</span>
                </div>

                <div class="cta-item">
                    <span class="note">Professional Network</span>
                    <a href="https://linkedin.com/in/shubhankar-negi-248a0920b" target="_blank" rel="noopener noreferrer" class="cta-value">LinkedIn Profile ↗</a>
                    <span class="note">shubhankar-negi-248a0920b</span>
                </div>
            </div>
        </section>

    </main>

    <!-- ===== SITE FOOTER ===== -->
    <footer class="site-footer wrap">
        <div class="footer-wrap">
            <div>
                <span>Shubhankar Negi · Full Stack Developer · Larsen &amp; Toubro (L&amp;T), Pune</span>
            </div>
            <div style="display:flex; gap:1.5rem; align-items:center;">
                <span>29.59° N, 79.65° E (Almora) · 18.52° N, 73.85° E (Pune)</span>
                <a href="#hero" class="note note--ink">↑ Back to Top</a>
            </div>
        </div>
    </footer>

    <!-- ===== DOCKED INTERACTIVE DEVELOPER TERMINAL (REPL) ===== -->
    <div class="dev-terminal-dock" id="devTerminal">
        <div class="terminal-titlebar" id="terminalTitlebar">
            <div class="terminal-titlebar-left">
                <i class="fa-solid fa-terminal" style="color:var(--accent-text);"></i>
                <span>shubhankar@pune-cluster:~</span>
            </div>
            <div class="terminal-actions">
                <button class="terminal-btn-icon" id="terminalMinBtn" title="Minimize/Maximize">_</button>
                <button class="terminal-btn-icon" id="terminalCloseBtn" title="Hide Terminal">×</button>
            </div>
        </div>
        <div class="terminal-body" id="terminalBody">
            <div class="terminal-chips">
                <button class="chip-btn" data-cmd="whoami">whoami</button>
                <button class="chip-btn" data-cmd="lnt">lnt-status</button>
                <button class="chip-btn" data-cmd="skills">skills</button>
                <button class="chip-btn" data-cmd="matrix">matrix</button>
                <button class="chip-btn" data-cmd="clear">clear</button>
            </div>
            <div class="terminal-output" id="terminalOutput">Welcome to Shubhankar's REPL shell.
Type 'help' or click the chips above to run commands.</div>
        </div>
        <div class="terminal-input-row">
            <span class="terminal-prompt">&gt;</span>
            <input type="text" class="terminal-input" id="terminalInput" placeholder="type a command (e.g. whoami, help)..." autocomplete="off" spellcheck="false">
        </div>
    </div>

    <!-- Floating Terminal Trigger (when docked terminal is closed) -->
    <button class="terminal-floating-pill" id="openTerminalPill">
        <i class="fa-solid fa-terminal" style="color:var(--accent-text);"></i>
        <span>&gt;_ REPL Terminal</span>
    </button>

    <!-- ===== COMMAND PALETTE OVERLAY (⌘K) ===== -->
    <div class="cmd-backdrop" id="cmdModal" aria-hidden="true">
        <div class="cmd-panel" onclick="event.stopPropagation()">
            <div class="cmd-input-bar">
                <i class="fa-solid fa-magnifying-glass note"></i>
                <input type="text" class="cmd-input" id="cmdInput" placeholder="Jump to section or action (e.g. work, resume, matrix, lnt)..." autocomplete="off">
                <span class="note">ESC</span>
            </div>
            <div class="cmd-list" id="cmdList">
                <div class="cmd-option" data-href="#hero"><span>00 // Overview (Home)</span><span class="note">00</span></div>
                <div class="cmd-option" data-href="#work"><span>01 // Selected Work &amp; L&amp;T Architecture</span><span class="note">01</span></div>
                <div class="cmd-option" data-href="#philosophy"><span>02 // Philosophy (Manifesto)</span><span class="note">02</span></div>
                <div class="cmd-option" data-href="#capabilities"><span>03 // Interactive REST API &amp; Stack</span><span class="note">03</span></div>
                <div class="cmd-option" data-href="#background"><span>04 // Education &amp; Credentials</span><span class="note">04</span></div>
                <div class="cmd-option" data-href="#interests"><span>05 // Beyond Code</span><span class="note">05</span></div>
                <div class="cmd-option" data-href="#contact"><span>06 // Contact &amp; Communication</span><span class="note">06</span></div>
                <div class="cmd-option" data-action="toggle-terminal"><span>Open Developer REPL Terminal</span><span class="note">&gt;_</span></div>
                <div class="cmd-option" data-action="toggle-matrix"><span>Toggle Matrix Digital Rain</span><span class="note">M</span></div>
                <div class="cmd-option" data-action="download-resume"><span>Download Resume (PDF)</span><span class="note">DL</span></div>
                <div class="cmd-option" data-action="toggle-theme"><span>Toggle Light/Dark Theme</span><span class="note">T</span></div>
                <div class="cmd-option" data-action="toggle-grid"><span>Toggle Blueprint Grid</span><span class="note">G</span></div>
            </div>
        </div>
    </div>

    <!-- ===== SCRIPT ENGINE ===== -->
    <script>
        // 0. Sound Effects Synthesis (Web Audio API - tactile clicks)
        let sfxEnabled = false;
        let audioCtx = null;

        function playTactileClick(freq = 900, duration = 0.02) {
            if (!sfxEnabled) return;
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch (e) {}
        }

        const soundBtn = document.getElementById('soundToggleBtn');
        const soundIcon = document.getElementById('soundIcon');
        soundBtn.addEventListener('click', () => {
            sfxEnabled = !sfxEnabled;
            soundIcon.className = sfxEnabled ? 'fa-solid fa-volume-high' : 'fa-solid fa-volume-xmark';
            if (sfxEnabled) playTactileClick(1200, 0.04);
        });

        // 1. Text Scramble / Decrypt Animation
        function scrambleElement(el) {
            const originalText = el.getAttribute('data-original-text') || el.textContent;
            if (!el.getAttribute('data-original-text')) {
                el.setAttribute('data-original-text', originalText);
            }
            const chars = '#@%&*01_/><~^+-=';
            let iterations = 0;
            const maxIterations = originalText.length * 2.2;

            if (el._scrambleInterval) clearInterval(el._scrambleInterval);

            el._scrambleInterval = setInterval(() => {
                el.textContent = originalText
                    .split('')
                    .map((char, index) => {
                        if (char === ' ' || char === '\n') return char;
                        if (index < iterations / 2.2) {
                            return originalText[index];
                        }
                        return chars[Math.floor(Math.random() * chars.length)];
                    })
                    .join('');

                iterations++;
                if (iterations > maxIterations) {
                    clearInterval(el._scrambleInterval);
                    el.textContent = originalText;
                }
            }, 30);
        }

        document.querySelectorAll('[data-scramble]').forEach(el => {
            el.setAttribute('data-original-text', el.textContent.trim());
            el.addEventListener('mouseenter', () => {
                playTactileClick(1100, 0.015);
                scrambleElement(el);
            });
        });

        // 2. High-Impact Architectural Compile Preloader
        (function initPreloader() {
            const preloader = document.getElementById('compilePreloader');
            const percentEl = document.getElementById('preloaderPercent');
            const progressBar = document.getElementById('preloaderProgressBar');
            const skipBtn = document.getElementById('skipPreloaderBtn');
            const logLines = [
                document.getElementById('log2'),
                document.getElementById('log3'),
                document.getElementById('log4'),
                document.getElementById('log5')
            ];

            let progress = 0;
            let finished = false;

            function finishPreloader() {
                if (finished) return;
                finished = true;
                progress = 100;
                percentEl.textContent = '100%';
                progressBar.style.width = '100%';
                setTimeout(() => {
                    preloader.classList.add('is-done');
                    // Scramble hero on entrance
                    const heroHuman = document.querySelector('.hero__human');
                    if (heroHuman) scrambleElement(heroHuman);
                }, 240);
            }

            skipBtn.addEventListener('click', finishPreloader);
            window.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && !finished) finishPreloader();
            });

            const interval = setInterval(() => {
                progress += Math.floor(Math.random() * 8) + 4;
                if (progress > 100) progress = 100;
                percentEl.textContent = (progress < 10 ? '0' : '') + progress + '%';
                progressBar.style.width = progress + '%';

                if (progress > 25 && logLines[0]) logLines[0].classList.add('active');
                if (progress > 50 && logLines[1]) logLines[1].classList.add('active');
                if (progress > 75 && logLines[2]) logLines[2].classList.add('active');
                if (progress > 90 && logLines[3]) logLines[3].classList.add('active');

                if (progress >= 100) {
                    clearInterval(interval);
                    finishPreloader();
                }
            }, 55);
        })();

        // 3. Precision Custom Cursor
        (function initCursor() {
            const cursor = document.getElementById('techCursor');
            const follower = document.getElementById('techCursorFollower');
            if (!cursor || !follower) return;

            let mouseX = -100, mouseY = -100;
            let followX = -100, followY = -100;

            window.addEventListener('mousemove', (e) => {
                mouseX = e.clientX;
                mouseY = e.clientY;
                cursor.style.left = mouseX + 'px';
                cursor.style.top = mouseY + 'px';
            });

            function render() {
                followX += (mouseX - followX) * 0.16;
                followY += (mouseY - followY) * 0.16;
                follower.style.left = followX + 'px';
                follower.style.top = followY + 'px';
                requestAnimationFrame(render);
            }
            render();

            document.querySelectorAll('a, button, [data-scrub], select, input').forEach(el => {
                el.addEventListener('mouseenter', () => document.body.classList.add('cursor-action'));
                el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-action'));
            });
        })();

        // 4. Scroll Ruler & Live Time Clock
        (function initHeaderHUD() {
            const ruler = document.getElementById('scrollRulerBar');
            const clock = document.getElementById('headerClock');

            window.addEventListener('scroll', () => {
                const total = document.documentElement.scrollHeight - window.innerHeight;
                const progress = total > 0 ? (window.scrollY / total) * 100 : 0;
                ruler.style.width = progress + '%';
            });

            function updateTime() {
                const now = new Date();
                const options = { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };
                clock.textContent = now.toLocaleTimeString('en-US', options) + ' IST';
            }
            setInterval(updateTime, 1000);
            updateTime();
        })();

        // 5. Scroll Reveal with IntersectionObserver
        (function initScrollReveal() {
            const reveals = document.querySelectorAll('.reveal-on-scroll');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('in-view');
                    }
                });
            }, { threshold: 0.12 });
            reveals.forEach(el => observer.observe(el));
        })();

        // 6. Interactive Hero Topographic Contour Canvas & Crosshair Axis HUD
        (function initTerrainAndCrosshair() {
            const hero = document.getElementById('hero');
            const canvas = document.getElementById('heroTerrainCanvas');
            const crosshair = document.getElementById('heroCrosshair');
            const axisX = document.getElementById('crosshairAxisX');
            const axisY = document.getElementById('crosshairAxisY');
            const target = document.getElementById('crosshairTarget');
            const label = document.getElementById('crosshairLabel');
            const elevationEl = document.getElementById('elevationDisplay');
            const coordsEl = document.getElementById('terrainCoords');

            if (!hero || !canvas) return;
            const ctx = canvas.getContext('2d');

            let width, height;
            let mouseX = -1000, mouseY = -1000;
            let targetElevation = 2420;
            let currentElevation = 2420;

            function resize() {
                width = canvas.width = hero.offsetWidth;
                height = canvas.height = hero.offsetHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            // Marching squares lookup table (16 cases)
            const msCases = [
                [], [[3, 2]], [[2, 1]], [[3, 1]],
                [[0, 1]], [[0, 3], [1, 2]], [[0, 2]], [[0, 3]],
                [[0, 3]], [[0, 2]], [[0, 1], [3, 2]], [[0, 1]],
                [[3, 1]], [[2, 1]], [[3, 2]], []
            ];

            // Grid resolution for smooth 60fps performance
            const cols = 56;
            const rows = 34;

            // Natural mountain peaks (Himalayan Almora & Pune terrain anchors)
            const peaks = [
                { nx: 0.28, ny: 0.42, amp: 1.35, sigma: 0.18 },
                { nx: 0.74, ny: 0.58, amp: 1.55, sigma: 0.22 },
                { nx: 0.50, ny: 0.26, amp: 1.15, sigma: 0.16 },
                { nx: 0.88, ny: 0.22, amp: 0.95, sigma: 0.14 }
            ];

            // 8 Contour elevation thresholds
            const thresholds = [0.38, 0.58, 0.78, 1.0, 1.25, 1.52, 1.82, 2.15];

            hero.addEventListener('mouseenter', () => {
                crosshair.classList.add('is-active');
                document.body.classList.add('in-hero-crosshair');
            });

            hero.addEventListener('mouseleave', () => {
                crosshair.classList.remove('is-active');
                document.body.classList.remove('in-hero-crosshair');
                mouseX = -1000;
                mouseY = -1000;
            });

            hero.addEventListener('mousemove', (e) => {
                const rect = hero.getBoundingClientRect();
                mouseX = e.clientX - rect.left;
                mouseY = e.clientY - rect.top;

                // Update crosshair axis positions
                axisX.style.transform = `translateY(${mouseY}px)`;
                axisY.style.transform = `translateX(${mouseX}px)`;
                target.style.transform = `translate(${mouseX - 6}px, ${mouseY - 6}px)`;
                label.style.transform = `translate(${mouseX + 18}px, ${mouseY + 12}px)`;

                // Exact format matching the design: X 1228 · Y 0340
                const xStr = String(Math.max(0, Math.round(e.clientX))).padStart(4, '0');
                const yStr = String(Math.max(0, Math.round(e.clientY))).padStart(4, '0');
                label.textContent = `X ${xStr} · Y ${yStr}`;

                targetElevation = 2200 + Math.round((mouseY / height) * 480);
                if (coordsEl) {
                    coordsEl.textContent = `Cursor · X: ${xStr} · Y: ${yStr} · Almora [29.59° N]`;
                }
            });

            let time = 0;
            function draw() {
                time += 0.012;
                ctx.clearRect(0, 0, width, height);

                currentElevation += (targetElevation - currentElevation) * 0.08;
                if (elevationEl) {
                    elevationEl.innerHTML = `<span class="note--accent">▲</span> terrain · elevation ${Math.round(currentElevation)}m · interactive`;
                }

                const isDark = document.documentElement.dataset.theme === 'dark';
                const baseColor = isDark ? '#508aff' : '#2f5bff';
                const cellW = width / cols;
                const cellH = height / rows;

                // Precompute 2D scalar field
                const field = [];
                for (let i = 0; i <= cols; i++) {
                    field[i] = [];
                    const x = i * cellW;
                    const nx = i / cols;
                    for (let j = 0; j <= rows; j++) {
                        const y = j * cellH;
                        const ny = j / rows;

                        let val = 0;
                        // Background peaks with gentle organic harmonic drift
                        for (let p = 0; p < peaks.length; p++) {
                            const pk = peaks[p];
                            const driftX = Math.sin(time + p * 1.5) * 0.03;
                            const driftY = Math.cos(time * 0.8 + p) * 0.03;
                            const dx = (nx - (pk.nx + driftX));
                            const dy = (ny - (pk.ny + driftY));
                            const d2 = dx * dx + dy * dy;
                            const sig2 = 2 * pk.sigma * pk.sigma;
                            val += pk.amp * Math.exp(-d2 / sig2);
                        }

                        // Ambient undulating harmonics
                        val += Math.sin(nx * 4.2 + time) * 0.12 + Math.cos(ny * 3.8 - time * 0.8) * 0.1;

                        // Dynamic cursor elevation perturbation (marching rings directly under cursor)
                        if (mouseX > -500) {
                            const dMouseX = (x - mouseX) / width;
                            const dMouseY = (y - mouseY) / height;
                            const dMouse2 = dMouseX * dMouseX + dMouseY * dMouseY;
                            // Mouse bump creates the tight concentric rings around crosshair
                            val += 1.85 * Math.exp(-dMouse2 / 0.032);
                        }

                        field[i][j] = val;
                    }
                }

                // Render contour isolines via Marching Squares
                ctx.save();
                ctx.shadowColor = isDark ? 'rgba(80, 138, 255, 0.45)' : 'rgba(47, 91, 255, 0.25)';
                ctx.shadowBlur = 5;

                for (let tIdx = 0; tIdx < thresholds.length; tIdx++) {
                    const T = thresholds[tIdx];
                    const isMajor = (tIdx % 2 === 1);

                    ctx.beginPath();
                    ctx.lineWidth = isMajor ? 2.4 : 1.3;
                    ctx.strokeStyle = isMajor
                        ? baseColor
                        : (isDark ? 'rgba(80, 138, 255, 0.65)' : 'rgba(47, 91, 255, 0.55)');

                    for (let i = 0; i < cols; i++) {
                        const x0 = i * cellW;
                        const x1 = (i + 1) * cellW;
                        for (let j = 0; j < rows; j++) {
                            const y0 = j * cellH;
                            const y1 = (j + 1) * cellH;

                            const v0 = field[i][j];
                            const v1 = field[i + 1][j];
                            const v2 = field[i + 1][j + 1];
                            const v3 = field[i][j + 1];

                            const bit0 = v0 >= T ? 8 : 0;
                            const bit1 = v1 >= T ? 4 : 0;
                            const bit2 = v2 >= T ? 2 : 0;
                            const bit3 = v3 >= T ? 1 : 0;
                            const code = bit0 | bit1 | bit2 | bit3;

                            if (code === 0 || code === 15) continue;

                            function getEdgePt(edge) {
                                if (edge === 0) {
                                    const t = (T - v0) / ((v1 - v0) || 0.0001);
                                    return [x0 + t * cellW, y0];
                                } else if (edge === 1) {
                                    const t = (T - v1) / ((v2 - v1) || 0.0001);
                                    return [x1, y0 + t * cellH];
                                } else if (edge === 2) {
                                    const t = (T - v3) / ((v2 - v3) || 0.0001);
                                    return [x0 + t * cellW, y1];
                                } else {
                                    const t = (T - v0) / ((v3 - v0) || 0.0001);
                                    return [x0, y0 + t * cellH];
                                }
                            }

                            const segs = msCases[code];
                            for (let s = 0; s < segs.length; s++) {
                                const pA = getEdgePt(segs[s][0]);
                                const pB = getEdgePt(segs[s][1]);
                                ctx.moveTo(pA[0], pA[1]);
                                ctx.lineTo(pB[0], pB[1]);
                            }
                        }
                    }
                    ctx.stroke();
                }

                ctx.restore();
                requestAnimationFrame(draw);
            }
            draw();
        })();

        // 7. Interactive Machine Token Typing Streamer
        (function initTokenStreamer() {
            const streamTarget = document.getElementById('streamTarget');
            const tokenEl = document.getElementById('tokenMetric');
            const latencyEl = document.getElementById('latencyMetric');
            const cycleBtn = document.getElementById('streamCycleBtn');

            const prompts = [
                "Full Stack Developer at <span class=\"highlight\">Larsen &amp; Toubro</span>, turning complex requirements into resilient production code.",
                "Computer vision developer optimizing <span class=\"highlight\">real-time OpenCV matrix pipelines</span> with 90% tested sketch accuracy.",
                "Backend engineer building <span class=\"highlight\">robust multi-tier Java &amp; Python services</span> with Tomcat &amp; MySQL architecture."
            ];

            let activeIdx = 0;
            let isStreaming = false;

            function streamText(htmlString) {
                if (isStreaming) return;
                isStreaming = true;
                streamTarget.innerHTML = '';
                const tokens = htmlString.split(' ');
                let tIdx = 0;
                tokenEl.textContent = tokens.length;
                latencyEl.textContent = (tokens.length * 28 + 60) + 'ms';

                const interval = setInterval(() => {
                    streamTarget.innerHTML += tokens[tIdx] + ' ';
                    playTactileClick(1400, 0.01);
                    tIdx++;
                    if (tIdx >= tokens.length) {
                        clearInterval(interval);
                        isStreaming = false;
                    }
                }, 40);
            }

            cycleBtn.addEventListener('click', () => {
                playTactileClick(800, 0.03);
                activeIdx = (activeIdx + 1) % prompts.length;
                streamText(prompts[activeIdx]);
            });
        })();

        // 8. 3-Stage Work Architecture Component with Live Interactive Simulations
        (function initWorkStages() {
            const projectData = [
                {
                    title: "Enterprise Full-Stack Architecture",
                    meta: "MAR 2026 — PRESENT · PUNE",
                    desc: "Engineering scalable microservices, responsive web views, and high-throughput API endpoints at Larsen & Toubro. Built for mission-critical reliability across multi-tenant enterprise workflows.",
                    tags: ["Full Stack Development", "Microservices", "REST APIs", "MySQL Cluster"],
                    plot: `[BROWSER CLIENT: HTML5/JS]\n  │ (HTTPS / JSON)\n  ▼\n[GATEWAY PROXY: TOMCAT/REVERSE-PROXY]\n  │\n  ├──▶ [SERVICE CONTROLLER: JAVA / SPRING / SERVLETS]\n  └──▶ [DATA REPOSITORY: MYSQL ACID PERSISTENCE]`,
                    build: `struct SystemDeployment {\n  organization: "Larsen & Toubro (L&T)",\n  role: "Full Stack Developer",\n  endpoints: "/api/v2/enterprise/telemetry",\n  throughput: "10k req/min",\n  persistence: "MySQL InnoDB + Indexed Keys"\n}`,
                    type: "lnt-sim"
                },
                {
                    title: "Real-Time Image to Sketch Converter",
                    meta: "PYTHON · OPENCV · 90% ACCURACY",
                    desc: "High-performance computer vision algorithm turning live webcam frames and static photographs into authentic pencil sketches using grayscale inversion and color dodge division.",
                    tags: ["Python", "OpenCV", "NumPy", "Computer Vision", "Matrix Blending"],
                    plot: `[RAW RGB CAMERA FRAME: (H, W, 3)]\n  │ (cv2.cvtColor: BGR2GRAY)\n  ▼\n[GRAYSCALE MATRIX: (H, W, 1)]\n  │ (cv2.bitwise_not: 255 - pixel)\n  ▼\n[INVERTED GAUSSIAN BLUR (21×21)]\n  │ (cv2.divide: color dodge blend)\n  ▼\n[PENCIL SKETCH MATRIX: 90% ACCURACY]`,
                    build: `def generate_sketch(frame_bgr):\n    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)\n    inv = cv2.bitwise_not(gray)\n    blur = cv2.GaussianBlur(inv, (21, 21), sigmaX=0)\n    return cv2.divide(gray, 255 - blur, scale=256.0)`,
                    type: "opencv-sim"
                },
                {
                    title: "Desktop Voice Assistant",
                    meta: "SPEECH RECOGNITION · AUTOMATION",
                    desc: "Voice-controlled intelligence platform capable of processing spoken natural language queries, running system automation commands, and answering queries via synthesized speech.",
                    tags: ["Python", "SpeechRecognition", "pyttsx3", "System Automation", "NLP"],
                    plot: `[MICROPHONE AUDIO STREAM: 44.1kHz]\n  │ (A/D sampling & ambient noise reduction)\n  ▼\n[SPEECH RECOGNITION PARSER]\n  │ (Intent extraction & NLP routing)\n  ▼\n[OS DISPATCHER] ──▶ [TTS ENGINE: pyttsx3 SYNTHESIS]`,
                    build: `class DesktopAssistant:\n    def __init__(self):\n        self.rec = sr.Recognizer()\n        self.engine = pyttsx3.init()\n    def listen_and_execute(self):\n        with sr.Microphone() as src:\n            audio = self.rec.listen(src)\n        return self.parse_intent(audio)`,
                    type: "voice-sim"
                },
                {
                    title: "Student Feedback Portal",
                    meta: "JAVA · SERVLETS · JSP · TOMCAT",
                    desc: "Multi-tier enterprise academic evaluation portal for Graphic Era Hill University. Collects and aggregates confidential student feedback across professors, courses, and department metrics.",
                    tags: ["Java", "JSP", "Servlets", "Apache Tomcat", "MySQL Database"],
                    plot: `[CLIENT: JSP & CSS3 RESPONSIVE VIEWS]\n  │ (HTTP POST: Encrypted evaluation token)\n  ▼\n[CONTROLLER: FeedbackServlet (Tomcat Container)]\n  │ (JDBC Transaction Isolation)\n  ▼\n[MYSQL PERSISTENCE: Indexed Evaluation Records]`,
                    build: `public class FeedbackServlet extends HttpServlet {\n    protected void doPost(HttpServletRequest req, HttpServletResponse res) {\n        Evaluation eval = parseForm(req);\n        dao.saveWithTransaction(eval);\n        res.sendRedirect("/dashboard/success");\n    }\n}`,
                    type: "feedback-sim"
                }
            ];

            let curProj = 0;
            let curStage = 'plot';

            const projectTabs = document.querySelectorAll('.ws-tab-btn');
            const stagePills = document.querySelectorAll('.stage-pill');
            const titleEl = document.getElementById('wsProjectTitle');
            const metaEl = document.getElementById('wsMetaDate');
            const descEl = document.getElementById('wsProjectDesc');
            const tagsEl = document.getElementById('wsTechTags');
            const plotEl = document.getElementById('plotDiagramText');
            const buildEl = document.getElementById('buildCodeText');
            const livePanel = document.getElementById('livePanelContent');

            function renderProject() {
                const p = projectData[curProj];
                titleEl.textContent = p.title;
                scrambleElement(titleEl);
                metaEl.textContent = p.meta;
                descEl.textContent = p.desc;
                tagsEl.innerHTML = p.tags.map(t => `<span class="work-tag">${t}</span>`).join('');
                plotEl.innerHTML = p.plot.replace(/\n/g, '<br>').replace(/ /g, '&nbsp;');
                buildEl.innerHTML = p.build.replace(/\n/g, '<br>').replace(/ /g, '&nbsp;');

                renderLiveSimulation(p);
            }

            function renderLiveSimulation(p) {
                if (p.type === 'lnt-sim') {
                    livePanel.innerHTML = `
                        <div class="packet-sim">
                            <div class="sim-node">
                                <div class="node-icon" id="nodeClient"><i class="fa-solid fa-desktop"></i></div>
                                <span>CLIENT</span>
                            </div>
                            <div class="sim-wire">
                                <div class="packet-dot" id="simPacketDot"></div>
                            </div>
                            <div class="sim-node">
                                <div class="node-icon" id="nodeGateway"><i class="fa-solid fa-server"></i></div>
                                <span>GATEWAY</span>
                            </div>
                            <div class="sim-node">
                                <div class="node-icon" id="nodeDb"><i class="fa-solid fa-database"></i></div>
                                <span>DATABASE</span>
                            </div>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="note" id="simStatusMsg">STATUS: IDLE · READY FOR PAYLOAD</span>
                            <button class="btn btn--ghost" id="fireSimBtn" style="height:2.4rem; padding-inline:1rem; font-size:0.8rem;">
                                Dispatch Request <i class="fa-solid fa-bolt" style="font-size:0.7rem; margin-left:4px;"></i>
                            </button>
                        </div>`;
                    document.getElementById('fireSimBtn').addEventListener('click', fireSim);
                } else if (p.type === 'opencv-sim') {
                    livePanel.innerHTML = `
                        <div class="sketch-interactive-box">
                            <div class="sketch-canvas-wrap">
                                <canvas id="opencvCanvas" width="400" height="220"></canvas>
                            </div>
                            <div class="opencv-controls">
                                <button class="filter-btn is-active" data-filter="original">1. Original RGB</button>
                                <button class="filter-btn" data-filter="gray">2. cv2.cvtColor Gray</button>
                                <button class="filter-btn" data-filter="blur">3. Gaussian Invert (21x21)</button>
                                <button class="filter-btn" data-filter="sketch">4. 90% Dodge Sketch</button>
                            </div>
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span class="note" id="cvMetricText">PIPELINE: RAW RGB INPUT (3 CHANNELS)</span>
                                <span class="note note--success">OPENCV 4.x ACTIVE</span>
                            </div>
                        </div>`;
                    initOpenCVCanvas();
                } else if (p.type === 'voice-sim') {
                    livePanel.innerHTML = `
                        <div class="voice-interactive-box">
                            <div class="voice-canvas-wrap">
                                <canvas id="voiceCanvas" width="400" height="90"></canvas>
                            </div>
                            <div class="voice-log-text" id="voiceLogText">&gt; Assistant standing by. Click 'Test Speech Command'.</div>
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <button class="btn btn--ghost" id="testVoiceBtn" style="height:2.4rem; padding-inline:1.1rem; font-size:0.8rem;">
                                    <i class="fa-solid fa-microphone"></i> Test Speech Command
                                </button>
                                <span class="note note--accent">TTS ENGINE: pyttsx3</span>
                            </div>
                        </div>`;
                    initVoiceCanvas();
                } else if (p.type === 'feedback-sim') {
                    livePanel.innerHTML = `
                        <div style="border:1px solid var(--line); padding:20px; border-radius:4px; background:var(--bg-surface); display:flex; flex-direction:column; gap:12px;">
                            <div style="display:flex; justify-content:space-between; font-family:var(--font-mono); font-size:0.75rem;">
                                <span>COURSE EVALUATION AGGREGATE</span>
                                <span class="note--accent">4.88 / 5.0 RATING</span>
                            </div>
                            <div style="height:6px; background:var(--line); border-radius:3px; overflow:hidden;">
                                <div style="width:94%; height:100%; background:var(--accent-text);"></div>
                            </div>
                            <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-family:var(--font-mono); font-size:0.72rem; color:var(--muted); margin-top:4px;">
                                <div>N = 340 Submissions</div>
                                <div>Apache Tomcat 9.0</div>
                                <div>MySQL InnoDB Engine</div>
                                <div class="note--success">Zero Deadlocks</div>
                            </div>
                        </div>`;
                }
            }

            function fireSim() {
                playTactileClick(900, 0.03);
                const dot = document.getElementById('simPacketDot');
                const status = document.getElementById('simStatusMsg');
                const nodeG = document.getElementById('nodeGateway');
                const nodeD = document.getElementById('nodeDb');
                if (!dot || !status) return;

                status.textContent = "ROUTING: DISPATCHING HTTP/2 TO TOMCAT GATEWAY...";
                dot.style.left = "48%";
                setTimeout(() => {
                    if (nodeG) nodeG.style.borderColor = 'var(--accent)';
                    dot.style.left = "96%";
                    status.textContent = "PERSISTED: MYSQL COMMIT (12ms) · HTTP 200 OK";
                    if (nodeD) nodeD.style.borderColor = 'var(--success)';
                    setTimeout(() => {
                        dot.style.left = "0%";
                        status.textContent = "STATUS: IDLE · READY FOR PAYLOAD";
                        if (nodeG) nodeG.style.borderColor = 'var(--line-strong)';
                        if (nodeD) nodeD.style.borderColor = 'var(--line-strong)';
                    }, 1400);
                }, 550);
            }

            // Interactive OpenCV Canvas Filter Pipeline
            function initOpenCVCanvas() {
                const cvCanvas = document.getElementById('opencvCanvas');
                if (!cvCanvas) return;
                const cvCtx = cvCanvas.getContext('2d');
                const metricText = document.getElementById('cvMetricText');
                const buttons = document.querySelectorAll('.filter-btn');

                let currentMode = 'original';

                function renderCVFrame() {
                    cvCtx.clearRect(0, 0, cvCanvas.width, cvCanvas.height);

                    // Draw procedural Himalayan mountain landscape frame
                    const w = cvCanvas.width;
                    const h = cvCanvas.height;

                    if (currentMode === 'original') {
                        // Rich RGB landscape
                        const grad = cvCtx.createLinearGradient(0, 0, 0, h);
                        grad.addColorStop(0, '#1e3a8a');
                        grad.addColorStop(0.5, '#f59e0b');
                        grad.addColorStop(1, '#065f46');
                        cvCtx.fillStyle = grad;
                        cvCtx.fillRect(0, 0, w, h);

                        // Sun
                        cvCtx.fillStyle = '#fef08a';
                        cvCtx.beginPath();
                        cvCtx.arc(w * 0.7, h * 0.3, 24, 0, Math.PI * 2);
                        cvCtx.fill();

                        // Mountains
                        cvCtx.fillStyle = '#1e293b';
                        cvCtx.beginPath();
                        cvCtx.moveTo(0, h);
                        cvCtx.lineTo(w * 0.25, h * 0.4);
                        cvCtx.lineTo(w * 0.5, h * 0.7);
                        cvCtx.lineTo(w * 0.75, h * 0.35);
                        cvCtx.lineTo(w, h);
                        cvCtx.fill();
                    } else if (currentMode === 'gray') {
                        // Grayscale
                        cvCtx.fillStyle = '#374151';
                        cvCtx.fillRect(0, 0, w, h);
                        cvCtx.fillStyle = '#9ca3af';
                        cvCtx.beginPath();
                        cvCtx.arc(w * 0.7, h * 0.3, 24, 0, Math.PI * 2);
                        cvCtx.fill();
                        cvCtx.fillStyle = '#111827';
                        cvCtx.beginPath();
                        cvCtx.moveTo(0, h);
                        cvCtx.lineTo(w * 0.25, h * 0.4);
                        cvCtx.lineTo(w * 0.5, h * 0.7);
                        cvCtx.lineTo(w * 0.75, h * 0.35);
                        cvCtx.lineTo(w, h);
                        cvCtx.fill();
                    } else if (currentMode === 'blur') {
                        // Inverted Gaussian Blur
                        cvCtx.fillStyle = '#d1d5db';
                        cvCtx.fillRect(0, 0, w, h);
                        cvCtx.fillStyle = '#6b7280';
                        cvCtx.filter = 'blur(6px)';
                        cvCtx.beginPath();
                        cvCtx.moveTo(0, h);
                        cvCtx.lineTo(w * 0.25, h * 0.4);
                        cvCtx.lineTo(w * 0.5, h * 0.7);
                        cvCtx.lineTo(w * 0.75, h * 0.35);
                        cvCtx.lineTo(w, h);
                        cvCtx.fill();
                        cvCtx.filter = 'none';
                    } else if (currentMode === 'sketch') {
                        // Pencil Sketch Dodge Output (90% tested accuracy)
                        cvCtx.fillStyle = '#f3f4f6';
                        cvCtx.fillRect(0, 0, w, h);
                        cvCtx.strokeStyle = '#111827';
                        cvCtx.lineWidth = 1.5;

                        // Mountain contours
                        cvCtx.beginPath();
                        cvCtx.moveTo(0, h);
                        cvCtx.lineTo(w * 0.25, h * 0.4);
                        cvCtx.lineTo(w * 0.5, h * 0.7);
                        cvCtx.lineTo(w * 0.75, h * 0.35);
                        cvCtx.lineTo(w, h);
                        cvCtx.stroke();

                        // Shading hatch lines
                        for (let x = 30; x < w * 0.45; x += 12) {
                            cvCtx.beginPath();
                            cvCtx.moveTo(x, h * 0.65);
                            cvCtx.lineTo(x + 10, h * 0.85);
                            cvCtx.stroke();
                        }
                    }
                }

                buttons.forEach(btn => {
                    btn.addEventListener('click', () => {
                        playTactileClick(1200, 0.02);
                        buttons.forEach(b => b.classList.remove('is-active'));
                        btn.classList.add('is-active');
                        currentMode = btn.dataset.filter;
                        renderCVFrame();

                        const msgs = {
                            original: "PIPELINE: RAW RGB INPUT (3 CHANNELS)",
                            gray: "PIPELINE: cv2.cvtColor(BGR2GRAY) SINGLE CHANNEL (8-BIT)",
                            blur: "PIPELINE: cv2.GaussianBlur(21×21) BITWISE NOT INVERSION",
                            sketch: "PIPELINE: cv2.divide() COLOR DODGE BLEND · 90% ACCURACY CONFIRMED"
                        };
                        metricText.textContent = msgs[currentMode];
                    });
                });

                renderCVFrame();
            }

            // Interactive Voice Waveform
            function initVoiceCanvas() {
                const voiceCanvas = document.getElementById('voiceCanvas');
                if (!voiceCanvas) return;
                const vCtx = voiceCanvas.getContext('2d');
                const logText = document.getElementById('voiceLogText');
                const testBtn = document.getElementById('testVoiceBtn');

                let isSpeaking = false;
                let animFrame = null;

                function drawWave(amplitude = 4) {
                    vCtx.clearRect(0, 0, voiceCanvas.width, voiceCanvas.height);
                    const w = voiceCanvas.width;
                    const h = voiceCanvas.height;
                    const bars = 38;
                    const barWidth = w / bars - 2;

                    for (let i = 0; i < bars; i++) {
                        const height = Math.sin(i * 0.25 + Date.now() * 0.008) * amplitude + amplitude + 4;
                        const y = (h - height) / 2;
                        vCtx.fillStyle = isSpeaking ? 'var(--accent-text)' : 'var(--line-strong)';
                        vCtx.fillRect(i * (barWidth + 2), y, barWidth, height);
                    }
                    animFrame = requestAnimationFrame(() => drawWave(isSpeaking ? 22 : 4));
                }
                drawWave();

                testBtn.addEventListener('click', () => {
                    playTactileClick(1000, 0.03);
                    if (isSpeaking) return;
                    isSpeaking = true;
                    logText.innerHTML = `<span class="note--accent">&gt; Listening...</span> Audio sampled via SpeechRecognition API`;

                    setTimeout(() => {
                        logText.innerHTML = `&gt; Recognized: <strong style="color:var(--ink);">"Query L&amp;T Pune cluster telemetry"</strong>`;
                        setTimeout(() => {
                            logText.innerHTML = `<span class="note--success">&gt; pyttsx3 TTS:</span> "System optimal. Uptime 99.98% across Pune nodes."`;
                            isSpeaking = false;
                        }, 1300);
                    }, 1200);
                });
            }

            projectTabs.forEach((tab, idx) => {
                tab.addEventListener('click', () => {
                    playTactileClick(1000, 0.02);
                    projectTabs.forEach(t => t.classList.remove('is-active'));
                    tab.classList.add('is-active');
                    curProj = idx;
                    renderProject();
                });
            });

            stagePills.forEach(pill => {
                pill.addEventListener('click', () => {
                    playTactileClick(1100, 0.02);
                    stagePills.forEach(p => p.classList.remove('is-active'));
                    pill.classList.add('is-active');
                    curStage = pill.dataset.stage;
                    document.querySelectorAll('.stage-view').forEach(v => v.classList.remove('is-visible'));
                    if (curStage === 'plot') document.getElementById('stagePlotView').classList.add('is-visible');
                    else if (curStage === 'build') document.getElementById('stageBuildView').classList.add('is-visible');
                    else if (curStage === 'live') document.getElementById('stageLiveView').classList.add('is-visible');
                });
            });

            renderProject();
        })();

        // 9. Interactive REST Client / Benchmark Probe
        (function initRestClient() {
            const endpointSelect = document.getElementById('restEndpointSelect');
            const sendBtn = document.getElementById('restSendBtn');
            const jsonDisplay = document.getElementById('restJsonDisplay');
            const statusVal = document.getElementById('restStatusVal');
            const latencyVal = document.getElementById('restLatencyVal');
            const sizeVal = document.getElementById('restSizeVal');
            const copyBtn = document.getElementById('copyJsonBtn');

            const payloads = {
                lnt: {
                    status: "200 OK",
                    size: "482 B",
                    json: `{\n  <span class="json-key">"organization"</span>: <span class="json-str">"Larsen & Toubro (L&T)"</span>,\n  <span class="json-key">"role"</span>: <span class="json-str">"Full Stack Developer"</span>,\n  <span class="json-key">"location"</span>: <span class="json-str">"Pune, Maharashtra"</span>,\n  <span class="json-key">"status"</span>: <span class="json-str">"Active (March 2026 — Present)"</span>,\n  <span class="json-key">"stack"</span>: [<span class="json-str">"Java"</span>, <span class="json-str">"Spring Boot"</span>, <span class="json-str">"MySQL"</span>, <span class="json-str">"Microservices"</span>],\n  <span class="json-key">"uptime"</span>: <span class="json-num">99.98</span>,\n  <span class="json-key">"verified"</span>: <span class="json-bool">true</span>\n}`
                },
                profile: {
                    status: "200 OK",
                    size: "524 B",
                    json: `{\n  <span class="json-key">"name"</span>: <span class="json-str">"Shubhankar Negi"</span>,\n  <span class="json-key">"education"</span>: <span class="json-str">"B.Tech CSE (Graphic Era Hill University)"</span>,\n  <span class="json-key">"locations"</span>: [<span class="json-str">"Pune, MH"</span>, <span class="json-str">"Almora, UK"</span>],\n  <span class="json-key">"email"</span>: <span class="json-str">"samnegi1844@gmail.com"</span>,\n  <span class="json-key">"phone"</span>: <span class="json-str">"+91 86500 51616"</span>,\n  <span class="json-key">"linkedin"</span>: <span class="json-str">"shubhankar-negi-248a0920b"</span>\n}`
                },
                cv: {
                    status: "200 OK",
                    size: "390 B",
                    json: `{\n  <span class="json-key">"project"</span>: <span class="json-str">"Real-Time Image to Sketch Converter"</span>,\n  <span class="json-key">"pipeline"</span>: <span class="json-str">"cv2.cvtColor -> GaussianBlur(21,21) -> cv2.divide"</span>,\n  <span class="json-key">"accuracy"</span>: <span class="json-str">"90% Tested"</span>,\n  <span class="json-key">"fps"</span>: <span class="json-num">60</span>,\n  <span class="json-key">"open_cv_version"</span>: <span class="json-str">"4.10.0"</span>\n}`
                },
                feedback: {
                    status: "200 OK",
                    size: "410 B",
                    json: `{\n  <span class="json-key">"project"</span>: <span class="json-str">"Student Feedback System"</span>,\n  <span class="json-key">"backend"</span>: <span class="json-str">"Java Servlets & JSP on Apache Tomcat"</span>,\n  <span class="json-key">"database"</span>: <span class="json-str">"MySQL InnoDB"</span>,\n  <span class="json-key">"evaluations_recorded"</span>: <span class="json-num">340</span>,\n  <span class="json-key">"latency_avg_ms"</span>: <span class="json-num">12.4</span>\n}`
                }
            };

            sendBtn.addEventListener('click', () => {
                playTactileClick(1300, 0.03);
                const ep = endpointSelect.value;
                const d = payloads[ep];
                statusVal.textContent = "SENDING...";
                statusVal.className = "meta-stat-val note--accent";

                setTimeout(() => {
                    statusVal.textContent = d.status;
                    statusVal.className = "meta-stat-val note--success";
                    latencyVal.textContent = (Math.floor(Math.random() * 8) + 10) + " ms";
                    sizeVal.textContent = d.size;
                    jsonDisplay.innerHTML = d.json;
                }, 160);
            });

            copyBtn.addEventListener('click', () => {
                const text = jsonDisplay.innerText;
                navigator.clipboard.writeText(text);
                copyBtn.textContent = "Copied!";
                setTimeout(() => copyBtn.textContent = "Copy JSON", 1500);
            });
        })();

        // 10. Code Inspector Tabs (Section 03)
        (function initCodeInspector() {
            const tabs = document.querySelectorAll('.code-tab-btn');
            const display = document.getElementById('codeDisplayArea');

            const snippets = {
                java: `<span class="cm">// Java Enterprise Servlet Controller</span>
<span class="kw">public class</span> FeedbackController <span class="kw">extends</span> HttpServlet {
    <span class="kw">private</span> FeedbackDAO feedbackDao = <span class="kw">new</span> FeedbackDAO();

    <span class="kw">protected void</span> doPost(HttpServletRequest req, HttpServletResponse resp) {
        String studentId = req.getParameter(<span class="st">"student_id"</span>);
        <span class="kw">int</span> instructorScore = Integer.parseInt(req.getParameter(<span class="st">"score"</span>));
        
        <span class="cm">// Validate payload & compute aggregate statistics</span>
        feedbackDao.recordMetric(studentId, instructorScore);
        resp.setStatus(HttpServletResponse.SC_OK);
    }
}`,
                python: `<span class="cm"># Python Computer Vision OpenCV Pipeline</span>
<span class="kw">import</span> cv2
<span class="kw">import</span> numpy <span class="kw">as</span> np

<span class="kw">def</span> <span class="fn">generate_sketch</span>(frame_bgr):
    <span class="cm"># 1. Grayscale & Bitwise Inversion</span>
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    
    <span class="cm"># 2. Gaussian Blur with 21x21 Kernel</span>
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)
    
    <span class="cm"># 3. Color Dodge Blending (Matrix Division)</span>
    <span class="kw">return</span> cv2.divide(gray, 255 - blurred, scale=256.0)`,
                sql: `<span class="cm">-- Relational Database Schema Architecture</span>
<span class="kw">CREATE TABLE</span> feedback_records (
    id <span class="kw">INT AUTO_INCREMENT PRIMARY KEY</span>,
    student_id <span class="kw">VARCHAR</span>(32) <span class="kw">NOT NULL</span>,
    instructor_id <span class="kw">VARCHAR</span>(32) <span class="kw">NOT NULL</span>,
    course_code <span class="kw">VARCHAR</span>(16) <span class="kw">NOT NULL</span>,
    score <span class="kw">TINYINT CHECK</span> (score <span class="kw">BETWEEN</span> 1 <span class="kw">AND</span> 5),
    submitted_at <span class="kw">TIMESTAMP DEFAULT CURRENT_TIMESTAMP</span>,
    <span class="kw">INDEX</span> idx_course (course_code),
    <span class="kw">INDEX</span> idx_instructor (instructor_id)
) <span class="kw">ENGINE</span>=InnoDB <span class="kw">DEFAULT CHARSET</span>=utf8mb4;`,
                devops: `<span class="cm"># Production Linux Deployment & Health Check</span>
<span class="fn">#!/usr/bin/env bash</span>
<span class="kw">set</span> -euo pipefail

<span class="kw">echo</span> <span class="st">"Deploying Tomcat artifact to L&T cluster..."</span>
systemctl stop tomcat9
cp target/enterprise-portal.war /var/lib/tomcat9/webapps/
systemctl start tomcat9

<span class="cm"># Verify 200 OK response on health probe</span>
curl -f -s -o /dev/null http://localhost:8080/enterprise-portal/health
<span class="kw">echo</span> <span class="st">"Deployment verified. Telemetry active."</span>`
            };

            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    playTactileClick(1100, 0.02);
                    tabs.forEach(t => t.classList.remove('is-active'));
                    tab.classList.add('is-active');
                    const lang = tab.dataset.lang;
                    display.innerHTML = snippets[lang];
                });
            });
        })();

        // 11. Docked Developer Interactive REPL Terminal
        (function initDevTerminal() {
            const terminal = document.getElementById('devTerminal');
            const titlebar = document.getElementById('terminalTitlebar');
            const minBtn = document.getElementById('terminalMinBtn');
            const closeBtn = document.getElementById('terminalCloseBtn');
            const input = document.getElementById('terminalInput');
            const output = document.getElementById('terminalOutput');
            const openPill = document.getElementById('openTerminalPill');
            const chipBtns = document.querySelectorAll('.chip-btn');

            let isMin = false;

            function toggleMin() {
                isMin = !isMin;
                terminal.classList.toggle('is-minimized', isMin);
                minBtn.textContent = isMin ? '□' : '_';
            }

            titlebar.addEventListener('click', (e) => {
                if (e.target === closeBtn) return;
                toggleMin();
            });

            minBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleMin();
            });

            closeBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                terminal.classList.add('is-hidden');
                openPill.style.display = 'flex';
            });

            openPill.addEventListener('click', () => {
                terminal.classList.remove('is-hidden');
                openPill.style.display = 'none';
                if (isMin) toggleMin();
                input.focus();
            });

            function executeCommand(rawCmd) {
                const cmd = rawCmd.trim().toLowerCase();
                if (!cmd) return;
                playTactileClick(1000, 0.02);

                output.innerHTML += `\n<span style="color:var(--accent-text);">&gt; ${rawCmd}</span>\n`;

                if (cmd === 'help') {
                    output.innerHTML += `Available commands:
• whoami       — Developer profile & current role
• lnt / status — L&T Pune cluster metrics & architecture
• skills       — Complete tech stack matrix
• projects     — Selected work overview
• matrix       — Toggle Matrix digital rain
• theme        — Toggle light / dark theme
• clear        — Clear terminal output`;
                } else if (cmd === 'whoami') {
                    output.innerHTML += `SHUBHANKAR NEGI
Role: Full Stack Developer @ Larsen & Toubro (L&T)
Locations: Pune, Maharashtra & Almora, Uttarakhand
Education: B.Tech CSE (Graphic Era Hill University, 2022–2025)
Email: samnegi1844@gmail.com · Tel: +91 86500 51616`;
                } else if (cmd === 'lnt' || cmd === 'status') {
                    output.innerHTML += `LARSEN & TOUBRO (L&T) CLUSTER TELEMETRY
Status: Active Production Node (March 2026 — Present)
Location: Pune, Maharashtra [18.52° N]
Stack: Java, Spring Boot, MySQL, REST APIs, Microservices
Uptime: 99.98% · Latency: 14ms · Memory: Nominal`;
                } else if (cmd === 'skills') {
                    output.innerHTML += `CORE TECHNICAL STACK:
• Languages: Java, Python, C++, C, SQL, JavaScript
• Backend: Spring Boot, Servlets, JSP, Tomcat, REST APIs
• Database: MySQL, Relational Design, Query Tuning, JDBC
• AI & Vision: OpenCV 4.x, NumPy, SpeechRecognition, pyttsx3
• DevOps: Linux CLI, Bash, Git, GitHub`;
                } else if (cmd === 'projects') {
                    output.innerHTML += `1. L&T Enterprise Platform (Full-Stack Architecture)
2. Real-Time Image to Sketch Converter (OpenCV, 90% Acc)
3. Desktop Assistant (Python, Voice & OS Automation)
4. Student Feedback System (Java, JSP, Tomcat, MySQL)`;
                } else if (cmd === 'matrix') {
                    toggleMatrixRain();
                    output.innerHTML += `Matrix digital rain overlay activated. Press ESC or button to exit.`;
                } else if (cmd === 'theme') {
                    const current = document.documentElement.dataset.theme;
                    setTheme(current === 'dark' ? 'light' : 'dark');
                    output.innerHTML += `Theme switched to: ${document.documentElement.dataset.theme.toUpperCase()}`;
                } else if (cmd === 'clear') {
                    output.innerHTML = `Terminal cleared. Type 'help' for commands.`;
                } else {
                    output.innerHTML += `command not found: '${rawCmd}'. Type 'help' for list.`;
                }

                output.scrollTop = output.scrollHeight;
                input.value = '';
            }

            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    executeCommand(input.value);
                }
            });

            chipBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const cmd = btn.getAttribute('data-cmd');
                    executeCommand(cmd);
                });
            });
        })();

        // 12. Matrix Digital Rain Overlay
        const matrixCanvas = document.getElementById('matrixCanvas');
        const mCtx = matrixCanvas.getContext('2d');
        const exitMatrixBtn = document.getElementById('exitMatrixBtn');
        let matrixInterval = null;

        function toggleMatrixRain() {
            document.body.classList.toggle('matrix-active');
            if (document.body.classList.contains('matrix-active')) {
                matrixCanvas.width = window.innerWidth;
                matrixCanvas.height = window.innerHeight;
                const cols = Math.floor(matrixCanvas.width / 16);
                const drops = Array(cols).fill(1);
                const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZアイウエオカキクケコサシスセソタチツテト';

                matrixInterval = setInterval(() => {
                    mCtx.fillStyle = 'rgba(0, 0, 0, 0.06)';
                    mCtx.fillRect(0, 0, matrixCanvas.width, matrixCanvas.height);
                    mCtx.fillStyle = '#00ff66';
                    mCtx.font = '14px monospace';

                    for (let i = 0; i < drops.length; i++) {
                        const char = chars[Math.floor(Math.random() * chars.length)];
                        mCtx.fillText(char, i * 16, drops[i] * 16);
                        if (drops[i] * 16 > matrixCanvas.height && Math.random() > 0.975) {
                            drops[i] = 0;
                        }
                        drops[i]++;
                    }
                }, 35);
            } else {
                clearInterval(matrixInterval);
                mCtx.clearRect(0, 0, matrixCanvas.width, matrixCanvas.height);
            }
        }

        exitMatrixBtn.addEventListener('click', toggleMatrixRain);
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && document.body.classList.contains('matrix-active')) {
                toggleMatrixRain();
            }
        });

        // 13. Theme Management (Light / Dark)
        const themeBtn = document.getElementById('themeToggleBtn');
        const themeLabel = document.getElementById('themeLabel');

        function setTheme(theme) {
            document.documentElement.dataset.theme = theme;
            localStorage.setItem('sn-theme', theme);
            themeLabel.textContent = theme.toUpperCase();
        }

        const savedTheme = localStorage.getItem('sn-theme') || 'dark';
        setTheme(savedTheme);

        themeBtn.addEventListener('click', () => {
            playTactileClick(1000, 0.02);
            const current = document.documentElement.dataset.theme;
            setTheme(current === 'dark' ? 'light' : 'dark');
        });

        // 14. Blueprint Grid Mode [G Key]
        const gridBtn = document.getElementById('gridToggleBtn');
        const hudDim = document.getElementById('hudDim');

        function updateDimensions() {
            if (hudDim) {
                hudDim.textContent = `VIEWPORT: ${window.innerWidth} × ${window.innerHeight}px · GRID 32px · NODE: ALMORA/PUNE`;
            }
        }
        window.addEventListener('resize', updateDimensions);
        updateDimensions();

        function toggleGrid() {
            document.body.classList.toggle('show-grid');
            gridBtn.classList.toggle('note--ink', document.body.classList.contains('show-grid'));
        }
        gridBtn.addEventListener('click', () => {
            playTactileClick(1000, 0.02);
            toggleGrid();
        });

        // 15. Command Palette (⌘K)
        const cmdModal = document.getElementById('cmdModal');
        const cmdToggleBtn = document.getElementById('cmdToggleBtn');
        const cmdInput = document.getElementById('cmdInput');
        const cmdList = document.getElementById('cmdList');

        function openCmd() {
            playTactileClick(1200, 0.02);
            cmdModal.classList.add('is-open');
            cmdInput.value = '';
            filterCmd('');
            setTimeout(() => cmdInput.focus(), 80);
        }

        function closeCmd() {
            cmdModal.classList.remove('is-open');
        }

        cmdToggleBtn.addEventListener('click', openCmd);
        cmdModal.addEventListener('click', closeCmd);

        window.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
                e.preventDefault();
                cmdModal.classList.contains('is-open') ? closeCmd() : openCmd();
            } else if (e.key === 'Escape' && cmdModal.classList.contains('is-open')) {
                closeCmd();
            } else if (e.key.toLowerCase() === 'g' && !['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) {
                toggleGrid();
            }
        });

        function filterCmd(q) {
            const query = q.toLowerCase().trim();
            cmdList.querySelectorAll('.cmd-option').forEach(opt => {
                opt.style.display = opt.textContent.toLowerCase().includes(query) ? 'flex' : 'none';
            });
        }
        cmdInput.addEventListener('input', (e) => filterCmd(e.target.value));

        cmdList.addEventListener('click', (e) => {
            const opt = e.target.closest('.cmd-option');
            if (!opt) return;

            playTactileClick(1100, 0.02);
            closeCmd();
            const href = opt.getAttribute('data-href');
            const action = opt.getAttribute('data-action');

            if (href) {
                document.querySelector(href)?.scrollIntoView({ behavior: 'smooth' });
            } else if (action === 'download-resume') {
                const a = document.createElement('a');
                a.href = 'Shubhankar_Negi_Resume.pdf';
                a.download = 'Shubhankar_Negi_Resume.pdf';
                a.click();
            } else if (action === 'toggle-theme') {
                const current = document.documentElement.dataset.theme;
                setTheme(current === 'dark' ? 'light' : 'dark');
            } else if (action === 'toggle-grid') {
                toggleGrid();
            } else if (action === 'toggle-matrix') {
                toggleMatrixRain();
            } else if (action === 'toggle-terminal') {
                const term = document.getElementById('devTerminal');
                term.classList.remove('is-hidden');
                document.getElementById('openTerminalPill').style.display = 'none';
                term.classList.remove('is-minimized');
                document.getElementById('terminalInput').focus();
            }
        });
    </script>
</body>
</html>'''

if __name__ == '__main__':
    with open('d:/Shubham Portfolio/index.html', 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print("Successfully generated enhanced interactive index.html!")

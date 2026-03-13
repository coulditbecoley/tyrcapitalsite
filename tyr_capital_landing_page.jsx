export default function TyrCapitalLandingPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <section className="relative overflow-hidden border-b border-white/10">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(59,130,246,0.18),transparent_35%),radial-gradient(circle_at_bottom_right,rgba(168,85,247,0.16),transparent_30%)]" />
        <div className="relative mx-auto max-w-6xl px-6 py-24 lg:px-8">
          <div className="max-w-3xl">
            <div className="mb-6 inline-flex items-center rounded-full border border-white/15 bg-white/5 px-4 py-1 text-sm text-white/80 backdrop-blur">
              Tyr Capital
            </div>
            <h1 className="text-4xl font-semibold tracking-tight sm:text-6xl">
              Disciplined Trading and Capital Management.
            </h1>
            <p className="mt-6 max-w-2xl text-lg leading-8 text-white/70">
              Tyr Capital is a private trading brand focused on structure, risk managment, and transparent market research.
            </p>
            <div className="mt-10 flex flex-wrap gap-4">
              <a
                href="#contact"
                className="rounded-2xl bg-white px-6 py-3 text-sm font-medium text-slate-950 shadow-lg shadow-white/10 transition hover:scale-[1.02]"
              >
                Contact Us
              </a>
              <a
                href="#services"
                className="rounded-2xl border border-white/15 bg-white/5 px-6 py-3 text-sm font-medium text-white transition hover:bg-white/10"
              >
                View Services
              </a>
            </div>
          </div>
        </div>
      </section>

      <section id="about" className="mx-auto max-w-6xl px-6 py-20 lg:px-8">
        <div className="grid gap-8 lg:grid-cols-2">
          <div className="rounded-3xl border border-white/10 bg-white/5 p-8 shadow-2xl shadow-black/20">
            <p className="text-sm uppercase tracking-[0.2em] text-blue-300">About</p>
            <h2 className="mt-4 text-3xl font-semibold">Built On Discipline and Clarity.</h2>
            <p className="mt-4 text-base leading-7 text-white/70">
              Tyr Capital presents a professional digital presence for a trading-focused brand.
            </p>
          </div>
          <div className="grid gap-6 sm:grid-cols-2">
            {[
              ["Risk Framework", "Structured approach to strategy, exposure, and review."],
              ["Market Research", "Share insights, outlooks, and macro commentary."],
              ["Performance Focus", "Highlight your process and long-term objectives."],
              ["Investor Ready", "A polished homepage for future business growth."],
            ].map(([title, text]) => (
              <div key={title} className="rounded-3xl border border-white/10 bg-slate-900 p-6">
                <h3 className="text-lg font-medium">{title}</h3>
                <p className="mt-3 text-sm leading-6 text-white/65">{text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="services" className="border-y border-white/10 bg-white/5">
        <div className="mx-auto max-w-6xl px-6 py-20 lg:px-8">
          <div className="max-w-2xl">
            <p className="text-sm uppercase tracking-[0.2em] text-purple-300">Services</p>
            <h2 className="mt-4 text-3xl font-semibold">Decisions are made using structured analysis rather than emotional reaction.</h2>
          </div>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            {[
              ["Strategy Overview", "Explain your approach, asset focus, and philosophy in plain language."],
              ["Research Notes", "Publish market updates, charts, or educational content for your audience."],
              ["Partnership Inquiries", "Give potential partners or clients a clear way to reach out."],
            ].map(([title, text]) => (
              <div key={title} className="rounded-3xl border border-white/10 bg-slate-950 p-7">
                <h3 className="text-xl font-medium">{title}</h3>
                <p className="mt-3 text-sm leading-6 text-white/65">{text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="contact" className="mx-auto max-w-6xl px-6 py-20 lg:px-8">
        <div className="rounded-[2rem] border border-white/10 bg-gradient-to-br from-white/10 to-white/5 p-10 shadow-2xl shadow-black/20">
          <p className="text-sm uppercase tracking-[0.2em] text-blue-300">Contact</p>
          <h2 className="mt-4 text-3xl font-semibold">Ready to launch Tyr Capital online?</h2>
          <p className="mt-4 max-w-2xl text-white/70">
            Tyr Capital is not a private fund and does not invest for others.
          </p>
          <div className="mt-8 flex flex-wrap gap-4 text-sm text-white/80">
            <span className="rounded-full border border-white/15 px-4 py-2">Email: tyrcapitalllc.com</span>
            <span className="rounded-full border border-white/15 px-4 py-2">Telegram Channel: Tyr Capital Trades</span>
          </div>
        </div>
      </section>
    </div>
  );
}

import './globals.css';

import Link from 'next/link';
import { Analytics } from '@vercel/analytics/react';
import { QuorumLogo } from '@/components/icons';
import { NavItem } from './nav-item';
import { Suspense } from 'react';
import Loading from './loading';

export const metadata = {
  title: 'Quorum',
  description: 'Coding Challenge'
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="h-full bg-gray-50">
      <body>
        <div className="grid min-h-screen w-full lg:grid-cols-[280px_1fr]">
          <div className="hidden border-r bg-gray-100/40 lg:block dark:bg-gray-800/40">
            <div className="flex h-full max-h-screen flex-col gap-2">
              <div className="flex h-[60px] items-center border-b px-5">
                <Link
                  className="flex items-center gap-2 font-semibold"
                  href="/"
                >
                  <QuorumLogo />
                </Link>
              </div>
              <div className="flex-1 overflow-auto py-2">
                <nav className="grid items-start px-4 text-sm font-medium">
                  <NavItem href="/">Home</NavItem>
                  <NavItem href="/legislators">Legislators</NavItem>
                  <NavItem href="/legislators_votes">Legislators Votes</NavItem>
                  <NavItem href="/bills_votes">Bills Votes</NavItem>
                  <NavItem href="https://github.com/mamude/quorum">
                    Github
                  </NavItem>
                </nav>
              </div>
            </div>
          </div>
          <div className="flex flex-col">
            <header className="flex h-14 lg:h-[60px] items-center gap-4 border-b bg-gray-100/40 px-6 dark:bg-gray-800/40 justify-between lg:justify-end">
              <Link
                className="flex items-center gap-2 font-semibold lg:hidden"
                href="/"
              >
                <QuorumLogo />
              </Link>
            </header>
            <Suspense fallback={<Loading />}>{children}</Suspense>
          </div>
        </div>
        <Analytics />
      </body>
    </html>
  );
}

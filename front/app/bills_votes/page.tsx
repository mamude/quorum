import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from '@/components/ui/table';

async function getBillsVotes() {
  const response = await fetch('http://localhost:8000/api/v1/bills/');

  if (!response.ok) {
    throw new Error('Failed to fetch data');
  }

  return response.json();
}

export default async function BillsVotesPage() {
  const bills = await getBillsVotes();
  return (
    <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-6">
      <div className="flex items-center">
        <h1 className="font-semibold text-lg md:text-2xl">Bills Votes</h1>
      </div>
      <div className="flex items-center">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>ID</TableHead>
              <TableHead>Bill</TableHead>
              <TableHead>Supporters</TableHead>
              <TableHead>Opposers</TableHead>
              <TableHead>Primary Sponsor</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {bills.map((l: any) => (
              <TableRow key={l.id}>
                <TableCell>{l.id}</TableCell>
                <TableCell>{l.bill}</TableCell>
                <TableCell>{l.supporters}</TableCell>
                <TableCell>{l.opposers}</TableCell>
                <TableCell>{l.primary_sponsor}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </main>
  );
}

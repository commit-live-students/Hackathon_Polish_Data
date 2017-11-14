# Hackathon_projects
## Problem   statement:
The   Financial   statement   of   a   firm   consists   of   critical   information   such   as   EBITDA   of   a   company,   which   can be   used   to   track   and   predict   the   future   of   a   company.   Although   important   information   is   also   present   in form   of   text   in   Notes   to   Financial   Statement   section   but,   here   we   are   simply   using   the   numeric information   for   the   prediction   purpose.

## Data:    The   dataset   is   about   bankruptcy   prediction   of   Polish   companies.   The   data   was   collected   from Emerging   Markets   Information   Service,   which   is   a   database   containing   information   on   emerging   markets around   the   world.   The   bankrupt   companies   were   analyzed   in   the   period   2000-2012,   while   the   still operating   companies   were   evaluated   from   2007   to   2013.

- Based   on   the   collected   data   five   classification   cases   were   distinguished,   that   depends   on   the forecasting   period:
    -   1stYear   :   the   data   contains   financial   rates   from   1st   year   of   the   forecasting   period   and corresponding   class   label   that   indicates   bankruptcy   status   after   5   years.   The   data   contains   7027 instances   (financial   statements),   271   represents   bankrupted   companies,   6756   firms   that   did   not bankrupt   in   the   forecasting   period.
    -   2ndYear   :   the   data   contains   financial   rates   from   2nd   year   of   the   forecasting   period   and corresponding   class   label   that   indicates   bankruptcy   status   after   4   years.   The   data   contains   10173 instances   (financial   statements),   400   represents   bankrupted   companies,   9773   firms   that   did   not bankrupt   in   the   forecasting   period.
    -   3rdYear   :   the   data   contains   financial   rates   from   3rd   year   of   the   forecasting   period   and corresponding   class   label   that   indicates   bankruptcy   status   after   3   years.   The   data   contains   10503 instances   (financial   statements),   495   represents   bankrupted   companies,   10008   firms   that   did not   bankrupt   in   the   forecasting   period.
    -   4thYear   :   the   data   contains   financial   rates   from   4th   year   of   the   forecasting   period   and corresponding   class   label   that   indicates   bankruptcy   status   after   2   years.   The   data   contains   9792 instances   (financial   statements),   515   represents   bankrupted   companies,   9277   firms   that   did   not bankrupt   in   the   forecasting   period.
    -   5thYear   :   the   data   contains   financial   rates   from   5th   year   of   the   forecasting   period   and corresponding   class   label   that   indicates   bankruptcy   status   after   1   year.   The   data   contains   5910 instances   (financial   statements),   410   represents   bankrupted   companies,   5500   firms   that   did   not bankrupt   in   the   forecasting   period.Train/Test   data   can   be   taken   as   a   mix   of   all   5   data   instances.

- Each   row   represents   a   company
- There   are   missing   values   which   will   have   to   be   dealt   with   during   Data   Preparation   stage
- For   classifying   into   train/test   a   mix   of   data   can   be   taken   from   the   5   categories.
- Some   key   attributes:
   1. X1   net   profit   /   total   assets
   2. X2   total   liabilities   /   total   assets
   3. X3   working   capital   /   total   assets
   4. X4   current   assets   /   short-term   liabilities
   5. X48   EBITDA   (profit   on   operating   activities   -   depreciation)   /   total   assets
   6. X49   EBITDA   (profit   on   operating   activities   -   depreciation)   /   sales


 ## Data Source: https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data
import { NgModule } from '@angular/core';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { AppConfirmComponent } from './app-confirm.component';
import { AppConfirmService } from './app-confirm.service';

@NgModule({
  imports: [
    MatDialogModule,
    MatButtonModule,
    FlexLayoutModule,
  ],
  exports: [AppConfirmComponent],
  declarations: [AppConfirmComponent],
  providers: [AppConfirmService],
  entryComponents: [AppConfirmComponent],
})
export class AppConfirmModule { }

//
//  CollectionViewCell.swift
//  SusGo_frontend
//
//  Created by Lily Pham on 10/15/22.
//

import SwiftUI

struct CollectionViewCell: View {
    static let column = 5
    static let row = 5
    
    let width = (UIScreen.main.bounds.width/5)-7
    let height = (UIScreen.main.bounds.height/5)-7
    
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 8).frame(width: width, height: width).foregroundColor(Color(0xA2DCEE)).offset(x: 0, y: 225)
            Text("ur mom").font(.headline).foregroundColor(.white).offset(x: 0, y: 225)
        }
    }
}

struct CollectionViewCell_Previews: PreviewProvider {
    static var previews: some View {
        CollectionViewCell()
    }
}
extension Color {
  init(_ hex: UInt, alpha: Double = 1) {
    self.init(
      .sRGB,
      red: Double((hex >> 16) & 0xFF) / 255,
      green: Double((hex >> 8) & 0xFF) / 255,
      blue: Double(hex & 0xFF) / 255,
      opacity: alpha
    )
  }
}
